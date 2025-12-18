import streamlit as st
import pandas as pd
import os
import io
from datetime import datetime
from pathlib import Path

st.set_page_config(layout="wide")

def validate_required_fields(fields):
    for field in fields:
        if field in [None, "", []]:
            st.warning("Παρακαλώ συμπληρώστε όλα τα απαραίτητα πεδία πριν συνεχίσετε.")
            st.stop()
            return False
    return True

# Ask for participant code
participant_code = st.text_input("Κωδικός Συμμετέχοντα", key="participant_code")

# Prevent continuing if it's empty
if not participant_code:
    st.warning("Παρακαλώ εισάγετε τον κωδικό συμμετέχοντα για να ξεκινήσετε.")
    st.stop()

# ΔΗΜΟΓΡΑΦΙΚΑ
st.title("Ερωτηματολόγιο")  # Survey title
st.markdown("## Δημογραφικά Στοιχεία")

age = st.number_input("Ηλικία", min_value=17, max_value=80, step=1, format="%d", value=None, placeholder="Πληκτρολογήστε την ηλικία σας", key="age")
gender = st.selectbox("Φύλο",["", "Γυναίκα", "Άντρας", "Μη-δυαδικό", "Προτιμώ να μην πω"],key="gender")

# Validation check
valid_demo = validate_required_fields([age, gender])

st.markdown("---")

# ΕΝΑΣΧΟΛΗΣΗ ΜΕ ΤΗ ΜΟΥΣΙΚΗ
st.markdown("## Ενασχόληση με τη Μουσική")

st.text_input(
    "Το μουσικό όργανο που παίζετε καλύτερα (συμπεριλαμβανομένης της φωνής) είναι:",
    key="instrument_goldmsi"
)

genre_listen_options = ["Ροκ/ποπ", "Τζαζ", "Κλασική", "Άλλο", "Κανένα"]

q1_music_style = st.radio(
    "Ποιο είδος μουσικής ακούτε περισσότερο;",
    genre_listen_options,
    index=None,
    key="q1_music_style"
)
if q1_music_style == "Άλλο":
    q1_music_style_other = st.text_input("Παρακαλώ διευκρινίστε:", key="q1_music_style_other")
else:
    q1_music_style_other = ""

genre_training_options = ["Ροκ/ποπ", "Τζαζ", "Κλασική", "Άλλο", "Κανένα"]

q_music_training_style = st.radio(
    "Σε ποιο είδος μουσικής έχετε λάβει εκπαίδευση ή είστε αυτοδίδακτος/η (αν δεν ισχύει για εσάς, επιλέξτε 'Κανένα');",
    genre_training_options,
    index=None,
    key="q_music_training_style"
)
if q_music_training_style == "Άλλο":
    q_music_training_style_other = st.text_input("Παρακαλώ διευκρινίστε:", key="q_music_training_style_other")
else:
    q_music_training_style_other = ""

q_learning = st.radio("Πώς αποκτήσατε τη μουσική σας εκπαίδευση/εμπειρία;", ["Επίσημη εκπαίδευση", "Αυτοδίδακτα", "Και τα δύο", "Δεν έχω μουσική εμπειρία"], index=None, key="q_learning")

# Validation check
valid_music = validate_required_fields(
    [
        st.session_state.get("instrument_goldmsi"),
        q1_music_style,
        q1_music_style_other if q1_music_style == "Άλλο" else "ok",
        q_music_training_style,
        q_music_training_style_other if q_music_training_style == "Άλλο" else "ok",
        q_learning,
    ]
)

st.markdown("---")

# ΕΜΠΕΙΡΙΑ ΜΕ ΑΥΤΟΣΧΕΔΙΑΣΜΟ
st.markdown("## Εμπειρία με τον αυτοσχεδιασμό")

q1_improv = st.radio(
    "Πόσο εξοικειωμένος/η αισθάνεστε με τον μουσικό αυτοσχεδιασμό;",
    ["1 (Καθόλου)", "2", "3", "4", "5", "6", "7 (Πάρα πολύ)"],
    index=None,
    key="q1_improv",
    horizontal=True
)

q2_improv = st.radio(
    "Πόσα χρόνια ασκείστε στον μουσικό αυτοσχεδιασμό;",
    ["0", "0.5", "1", "2", "3", "4-6", "7-10", "11 ή περισσότερα"],
    index=None,
    key="q2_improv", horizontal=True,
)

q3_improv = st.multiselect(
    "Με ποιον τρόπο εξοικειωθήκατε με τον αυτοσχεδιασμό; (Μπορείτε να επιλέξετε περισσότερες από μία επιλογές)",
    ["Επίσημη εκπαίδευση", "Αυτοδίδακτος/η", "Παίζοντας σε σύνολο/ομάδα", "Παίζοντας μόνος/η μου", "Άλλο"],
    key="q3_improv"
)
if "Άλλο" in q3_improv:
    q3_improv_other = st.text_input("Παρακαλώ διευκρινίστε:", key="q3_improv_other")
else:
    q3_improv_other = ""

q4_improv = st.radio(
    "Πόσες φορές έχετε αυτοσχεδιάσει ζωντανά (σε κοινό);",
    ["0", "1", "2-5", "6-10", "11-20", "21 ή περισσότερες"],
    index=None,
    key="q4_improv", horizontal=True,
)

# Validation check
valid_improv = validate_required_fields([q1_improv,q2_improv,q3_improv,q3_improv_other if "Άλλο" in q3_improv else "ok",q4_improv,])

st.markdown("---")

# GOLD-MSI
st.markdown("## Μουσική εκπαίδευση")
st.markdown("**Παρακαλώ επιλέξτε αυτό που σας ταιριάζει περισσότερο.**")

likert_options = ["Συμφωνώ απόλυτα", "Συμφωνώ πολύ", "Συμφωνώ", "Ούτε συμφωνώ ούτε διαφωνώ",
    "Διαφωνώ", "Διαφωνώ πολύ", "Διαφωνώ απόλυτα"]

q1_goldmsi_mt = st.radio("Ποτέ δεν έχω λάβει κοπλιμέντα για τα ταλέντα μου ως μουσικός ερμηνευτής.", likert_options, index=None, key="q1_goldmsi_mt", horizontal=True)
q2_goldmsi_mt = st.radio("Δεν θα θεωρούσα τον εαυτό μου μουσικό.", likert_options, index=None, key="q2_goldmsi_mt", horizontal=True)
q3_goldmsi_mt = st.radio("Έκανα τακτική, καθημερινή εξάσκηση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) για ___ χρόνια.", ["0", "1", "2", "3", "4-5", "6-9", "10 ή περισσότερα"], index=None, horizontal=True, key="q3_goldmsi_mt")
q4_goldmsi_mt = st.radio("Στο αποκορύφωμα του ενδιαφέροντός μου, μελετούσα ___ ώρες την ημέρα το κύριο όργανό μου.", ["0", "0,5", "1", "1,5", "2", "3-4", "5 ή περισσότερες"], index=None, horizontal=True, key="q4_goldmsi_mt")
q5_goldmsi_mt = st.radio("Έχω λάβει επίσημα μαθήματα θεωρίας της μουσικής __ χρόνια.", ["0", "0,5", "1", "2", "3", "4-6", "7 ή περισσότερα"], index=None, horizontal=True, key="q5_goldmsi_mt")
q6_goldmsi_mt = st.radio("Έχω λάβει __ χρόνια επίσημη εκπαίδευση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) κατά τη διάρκεια της ζωής μου.", ["0", "0,5", "1", "2", "3-5", "6-9", "10 ή περισσότερα"], index=None, horizontal=True, key="q6_goldmsi_mt")
q7_goldmsi_mt = st.radio("Μπορώ να παίξω ___ μουσικά όργανα.", ["0", "1", "2", "3", "4", "5", "6 ή περισσότερα"], index=None, horizontal=True, key="q7_goldmsi_mt")

# Validation check
valid_goldmsi_mt = validate_required_fields(
    [
        q1_goldmsi_mt,
        q2_goldmsi_mt,
        q3_goldmsi_mt,
        q4_goldmsi_mt,
        q5_goldmsi_mt,
        q6_goldmsi_mt,
        q7_goldmsi_mt,
    ]
)

st.markdown("---")

# TIPI
st.markdown("## Προσωπικότητα")
st.markdown("**Θεωρώ τον εαυτό μου:**")
st.markdown("**1 = Διαφωνώ απόλυτα  2 = Διαφωνώ μέτρια  3 = Διαφωνώ λίγο  4 = Δεν συμφωνώ ούτε διαφωνώ  5 = Συμφωνώ λίγο  6 = Συμφωνώ μέτρια  7 = Συμφωνώ απόλυτα**")

tipi_options = ["1", "2", "3", "4", "5", "6", "7"]

q1_tipi = st.radio("Εξωστρεφή, ενθουσιώδη", tipi_options, index=None, key="q1_tipi", horizontal=True)
q2_tipi = st.radio("Επικριτικό, εριστικό", tipi_options, index=None, key="q2_tipi", horizontal=True)
q3_tipi = st.radio("Αξιόπιστο, πειθαρχημένο", tipi_options, index=None, key="q3_tipi", horizontal=True)
q4_tipi = st.radio("Αγχώδη, αναστατώνεται εύκολα", tipi_options, index=None, key="q4_tipi", horizontal=True)
q5_tipi = st.radio("Ανοιχτό σε νέες εμπειρίες, περίπλοκο", tipi_options, index=None, key="q5_tipi", horizontal=True)
q6_tipi = st.radio("Συγκρατημένο, ήσυχο", tipi_options, index=None, key="q6_tipi", horizontal=True)
q7_tipi = st.radio("Συμπαθητικό, ζεστό", tipi_options, index=None, key="q7_tipi", horizontal=True)
q8_tipi = st.radio("Ανοργάνωτο, απρόσεκτο", tipi_options, index=None, key="q8_tipi", horizontal=True)
q9_tipi = st.radio("Ήρεμο, συναισθηματικά σταθερό", tipi_options, index=None, key="q9_tipi", horizontal=True)
q10_tipi = st.radio("Συμβατικό, μη δημιουργικό", tipi_options, index=None, key="q10_tipi", horizontal=True)

valid_tipi = validate_required_fields(
    [
        q1_tipi,
        q2_tipi,
        q3_tipi,
        q4_tipi,
        q5_tipi,
        q6_tipi,
        q7_tipi,
        q8_tipi,
        q9_tipi,
        q10_tipi,
    ]
)

st.markdown("---")

# Νοοτροπία για τη Δημιουργικότητα
st.markdown("## Νοοτροπία για τη Δημιουργικότητα")
st.markdown("**Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.**")
st.markdown("**1 = Σίγουρα όχι  5 = Σίγουρα ναι**")

cms_options = ["1", "2", "3", "4", "5"]

q1_cms = st.radio("Ο καθένας μπορεί να δημιουργήσει κάτι σπουδαίο κάποια στιγμή, αν του/της δοθούν οι κατάλληλες συνθήκες", cms_options, index=None, key="q1_mindset", horizontal=True)
q2_cms = st.radio("Είτε είναι κανείς δημιουργικός είτε δεν είναι - ακόμα κι αν προσπαθήσει πολύ σκληρά δεν μπορεί να αλλάξει πολύ", cms_options, index=None, key="q2_mindset", horizontal=True)
q3_cms = st.radio("Ο καθένας/η καθεμία μπορεί να αναπτύξει τις δημιουργικές του/της ικανότητες μέχρι ένα σημείο", cms_options, index=None, key="q3_mindset", horizontal=True)
q4_cms = st.radio("Πρέπει να είσαι γεννημένος/η δημιουργός - χωρίς έμφυτο ταλέντο μπορείς μόνο να είσαι κακότεχνος", cms_options, index=None, key="q4_mindset", horizontal=True)
q5_cms = st.radio("Η εξάσκηση τελειοποιεί - η επιμονή και η σκληρή προσπάθεια είναι οι καλύτεροι τρόποι να αναπτύξει και να επεκτείνει κάποιος/α τις ικανότητές του/της", cms_options, index=None, key="q5_mindset", horizontal=True)
q6_cms = st.radio("Η δημιουργικότητα μπορεί να αναπτυχθεί, αλλά κάποιος/α είτε είναι είτε δεν είναι ένα πραγματικά δημιουργικό άτομο", cms_options, index=None, key="q6_mindset", horizontal=True)
q7_cms = st.radio("Η Ρώμη δεν χτίστηκε σε μια μέρα - κάθε δημιουργικό έργο απαιτεί προσπάθεια και δουλειά, και αυτά τα δύο είναι πιο σημαντικά από το ταλέντο", cms_options, index=None, key="q7_mindset", horizontal=True)
q8_cms = st.radio("Μερικοί άνθρωποι είναι δημιουργικοί, άλλοι δεν είναι - και καμία εξάσκηση δεν μπορεί να το αλλάξει", cms_options, index=None, key="q8_mindset", horizontal=True)
q9_cms = st.radio("Δεν έχει σημασία ποιο επίπεδο δημιουργικότητας επιδεικνύει κάποιος - μπορείς πάντα να το αυξήσεις", cms_options, index=None, key="q9_mindset", horizontal=True)
q10_cms = st.radio("Το πραγματικά δημιουργικό ταλέντο είναι έμφυτο και σταθερό σε ολόκληρη τη ζωή του ατόμου", cms_options, index=None, key="q10_mindset", horizontal=True)

st.markdown("**1 = Σίγουρα όχι  5 = Σίγουρα ναι**")

valid_cms = validate_required_fields([
    q1_cms, q2_cms, q3_cms, q4_cms, q5_cms,
    q6_cms, q7_cms, q8_cms, q9_cms, q10_cms
])

st.markdown("---")

if st.button("Υποβολή απαντήσεων"):
    responses = {key: value for key, value in st.session_state.items()}
    responses["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Set up dynamic filename
    directory = Path("data")
    filename = f"{participant_code}_survey_responses.csv"
    filepath = directory / filename

    directory.mkdir(parents=True, exist_ok=True)
    file_exists = filepath.exists()

    df = pd.DataFrame([responses])

    # Save locally
    df.to_csv(filepath, index=False, mode="a", header=not file_exists)

    st.success("Οι απαντήσεις σας καταχωρήθηκαν. Ευχαριστούμε!")

    # Generate downloadable CSV in memory
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    download_filename = f"{participant_code}_survey_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"

    st.download_button(
        label="📥 Κατεβάστε τις απαντήσεις σας",
        data=csv_data,
        file_name=download_filename,
        mime="text/csv"
    )
