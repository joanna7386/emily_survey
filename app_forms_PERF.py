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

age = st.number_input("Ηλικία", min_value=17, max_value=80, step=1, format="%d", value=None, placeholder="Πληκτρολογήστε την ηλικία σας")
gender = st.selectbox("Φύλο",["", "Γυναίκα", "Άντρας", "Μη-δυαδικό", "Προτιμώ να μην πω"])

# Validation check
valid_demo = validate_required_fields([age, gender])

st.markdown("---")

# ΕΝΑΣΧΟΛΗΣΗ ΜΕ ΤΗ ΜΟΥΣΙΚΗ
st.markdown("## Ενασχόληση με τη Μουσική")

st.text_input(
    "Το μουσικό όργανο που παίζω καλύτερα (συμπεριλαμβανομένης της φωνής) είναι:",
    placeholder="π.χ. πιάνο, κιθάρα, φλάουτο, φωνή",
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

q_learning = st.radio("Πώς αποκτήσατε τη μουσική σας εκπαίδευση/εμπειρία;", ["Επίσημη εκπαίδευση", "Αυτοδίδακτα", "Και τα δύο", "Δεν έχω μουσική εμπειρία"], index=None)

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
st.markdown("**Βλέπω τον εαυτό μου ως:**")
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

# IRI
st.markdown("## Διαπροσωπική Ανταπόκριση")
st.markdown("**Για κάθε δήλωση, προσδιορίστε πόσο καλά σας χαρακτηρίζει:**")
st.markdown("**A = ΔΕΝ ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΚΑΘΟΛΟΥ  E = ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΠΟΛΥ**")

iri_options = ["Α", "Β", "Γ", "Δ", "Ε"]

q1_iri = st.radio("Συχνά ονειροπολώ και φαντάζομαι πράγματα που μπορεί να μου συμβούν", iri_options, index=None, key="q1_iri", horizontal=True)
q5_iri = st.radio("Εντρυφώ πραγματικά στα συναισθήματα των προσώπων ενός μυθιστορήματος", iri_options, index=None, key="q5_iri", horizontal=True)
q7_iri = st.radio("Συνήθως προσπαθώ να είμαι αντικειμενικός/η όταν παρακολουθώ ένα κινηματογραφικό ή ένα θεατρικό έργο και δεν παρασύρομαι από αυτό", iri_options, index=None, key="q7_iri", horizontal=True)
q12_iri = st.radio("Είναι σπάνιες οι φορές που με απορροφά ένα καλό βιβλίο ή έργο", iri_options, index=None, key="q12_iri", horizontal=True)
q16_iri = st.radio("Μετά από ένα θεατρικό έργο ή μια ταινία αισθάνομαι σαν να ήμουν ένας από τους πρωταγωνιστές", iri_options, index=None, key="q16_iri", horizontal=True)
q23_iri = st.radio("Όταν βλέπω ένα καλό έργο ταυτίζομαι εύκολα με τον πρωταγωνιστή", iri_options, index=None, key="q23_iri", horizontal=True)
q26_iri = st.radio("Όταν διαβάζω μια ενδιαφέρουσα ιστορία προσπαθώ να φανταστώ πως θα αισθανόμουν αν τα γεγονότα της ιστορίας συνέβαιναν σε μένα", iri_options, index=None, key="q26_iri", horizontal=True)

valid_iri = validate_required_fields([
    q1_iri, q5_iri, q7_iri, q12_iri, q16_iri, q23_iri, q26_iri
])

st.markdown("---")

# EMOTCONT
st.markdown("## Συναισθηματική Μετάδοση")
st.markdown("**Απάντησε σύμφωνα με τον δικό σου τρόπο να σκέφτεσαι, να αισθάνεσαι και να ενεργείς σε διάφορες καταστάσεις:**")
st.markdown("**1 = Ποτέ  5 = Πάντα**")

emotcont_options = ["1", "2", "3", "4", "5"]

q1_emotcont = st.radio("1. Εάν ο συνομιλητής μου αρχίζει να κλαίει, τότε μου έρχονται δάκρυα στα μάτια.", emotcont_options, index=None, key="q1_emotcont", horizontal=True)
q2_emotcont = st.radio("2. Το να είμαι με κάποιον που είναι χαρούμενος, με κάνει να αισθάνομαι καλύτερα όταν είμαι στεναχωρημένος.", emotcont_options, index=None, key="q2_emotcont", horizontal=True)
q3_emotcont = st.radio("3. Όταν κάποιος μου χαμογελά εγκάρδια, ανταποδίδω το χαμόγελό του και αισθάνομαι όμορφα μέσα μου.", emotcont_options, index=None, key="q3_emotcont", horizontal=True)
q4_emotcont = st.radio("4. Γεμίζω με συναισθήματα λύπης όταν κάποιος μου διηγείται τον θάνατο κάποιου αγαπημένου του προσώπου.", emotcont_options, index=None, key="q4_emotcont", horizontal=True)
q5_emotcont = st.radio("5. Σφίγγω τα δόντια μου και τους ώμους μου, όταν βλέπω θυμωμένα πρόσωπα στις ειδήσεις.", emotcont_options, index=None, key="q5_emotcont", horizontal=True)
q6_emotcont = st.radio("6. Όταν κοιτάζω μέσα στα μάτια τους αγαπημένους μου, καταλαμβάνομαι από ρομαντικές σκέψεις.", emotcont_options, index=None, key="q6_emotcont", horizontal=True)
q7_emotcont = st.radio("7. Εκνευρίζομαι όταν βρίσκομαι μεταξύ θυμωμένων ανθρώπων.", emotcont_options, index=None, key="q7_emotcont", horizontal=True)
q8_emotcont = st.radio("8. Όταν βλέπω τα φοβισμένα πρόσωπα των θυμάτων στις ειδήσεις, προσπαθώ να φανταστώ το πώς αισθάνονται.", emotcont_options, index=None, key="q8_emotcont", horizontal=True)
q9_emotcont = st.radio("9. «Λιώνω», όταν αυτός/ή που αγαπώ με αγκαλιάζει.", emotcont_options, index=None, key="q9_emotcont", horizontal=True)
q10_emotcont = st.radio("10. Φορτίζομαι όταν τυχαίνει να ακούσω έναν καβγά.", emotcont_options, index=None, key="q10_emotcont", horizontal=True)
q11_emotcont = st.radio("11. Όταν περιτριγυρίζομαι από χαρούμενους ανθρώπους, γεμίζω με χαρούμενες σκέψεις.", emotcont_options, index=None, key="q11_emotcont", horizontal=True)
q12_emotcont = st.radio("12. Το αισθάνομαι σε όλο το σώμα, όταν ο/η αγαπημένος/η μου με αγγίζει.", emotcont_options, index=None, key="q12_emotcont", horizontal=True)
q13_emotcont = st.radio("13. Καταλαβαίνω ότι φορτίζομαι όταν βρίσκομαι μεταξύ ανήσυχων ανθρώπων.", emotcont_options, index=None, key="q13_emotcont", horizontal=True)
q14_emotcont = st.radio("14. Κλαίω, όταν βλέπω λυπητερά έργα.", emotcont_options, index=None, key="q14_emotcont", horizontal=True)
q15_emotcont = st.radio("15. Εάν τύχει να ακούσω την κραυγή ενός τρομαγμένου παιδιού, στην αίθουσα αναμονής του οδοντιατρείου, γίνομαι νευρικός/ή.", emotcont_options, index=None, key="q15_emotcont", horizontal=True)

st.markdown("**1 = Ποτέ  5 = Πάντα**")

valid_emotcont = validate_required_fields([
    q1_emotcont, q2_emotcont, q3_emotcont, q4_emotcont, q5_emotcont,
    q6_emotcont, q7_emotcont, q8_emotcont, q9_emotcont, q10_emotcont,
    q11_emotcont, q12_emotcont, q13_emotcont, q14_emotcont, q15_emotcont
])

st.markdown("---")

# ΣΥΝΑΙΣΘΗΜΑΤΙΚΗ ΚΑΤΑΣΤΑΣΗ
st.markdown("## Πώς αισθάνεστε τώρα")

# Free text response — no placeholder to avoid priming
q1_mood_open = st.text_area(
    "Πώς αισθάνεστε σήμερα; Τι διάθεση έχετε;",
    key="q1_mood_open"
)

# Valence (without label)
q2_valence = st.slider(
    "Πόσο θετικά ή αρνητικά αισθάνεστε αυτή τη στιγμή;",
    min_value=1,
    max_value=7,
    value=4,
    format="%d",
    key="q2_valence"
)
st.caption("1 = Πολύ αρνητικά, 7 = Πολύ θετικά")

# Arousal (without label)
q3_arousal = st.slider(
    "Πόσο ενεργοποιημένος/η ή ήρεμος/η αισθάνεστε αυτή τη στιγμή;",
    min_value=1,
    max_value=7,
    value=4,
    format="%d",
    key="q3_arousal"
)
st.caption("1 = Πολύ ήρεμος/η, 7 = Πολύ ενεργοποιημένος/η")

valid_mood = validate_required_fields([q1_mood_open, q2_valence, q3_arousal])

st.markdown("---")

# BMIS
st.markdown("## Διάθεση")
st.markdown("**Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.**")
st.markdown("**1 = Σίγουρα δεν νιώθω  7 = Σίγουρα νιώθω**")

bmis_options = ["1", "2", "3", "4", "5", "6", "7"]

q1_bmis = st.radio("Ζωντανός/ή", bmis_options, index=None, key="q1_mood", horizontal=True)
q2_bmis = st.radio("Χαρούμενος/η", bmis_options, index=None, key="q2_mood", horizontal=True)
q3_bmis = st.radio("Λυπημένος/η", bmis_options, index=None, key="q3_mood", horizontal=True)
q4_bmis = st.radio("Κουρασμένος/η", bmis_options, index=None, key="q4_mood", horizontal=True)
q5_bmis = st.radio("Στοργικός/ή", bmis_options, index=None, key="q5_mood", horizontal=True)
q6_bmis = st.radio("Ικανοποιημένος/η", bmis_options, index=None, key="q6_mood", horizontal=True)
q7_bmis = st.radio("Κατηφής", bmis_options, index=None, key="q7_mood", horizontal=True)
q8_bmis = st.radio("Νευρικός/ή", bmis_options, index=None, key="q8_mood", horizontal=True)
q9_bmis = st.radio("Νυσταγμένος/η", bmis_options, index=None, key="q9_mood", horizontal=True)
q10_bmis = st.radio("Γκρινιάρης/α", bmis_options, index=None, key="q10_mood", horizontal=True)
q11_bmis = st.radio("Ζωηρός", bmis_options, index=None, key="q11_mood", horizontal=True)
q12_bmis = st.radio("Αγχωμένος/η", bmis_options, index=None, key="q12_mood", horizontal=True)
q13_bmis = st.radio("Ήρεμος/η", bmis_options, index=None, key="q13_mood", horizontal=True)
q14_bmis = st.radio("Τρυφερός/ή", bmis_options, index=None, key="q14_mood", horizontal=True)
q15_bmis = st.radio("Απαυδισμένος/η", bmis_options, index=None, key="q15_mood", horizontal=True)
q16_bmis = st.radio("Δραστήριος/α", bmis_options, index=None, key="q16_mood", horizontal=True)

st.markdown("**1 = Σίγουρα δεν νιώθω  7 = Σίγουρα νιώθω**")

valid_bmis = validate_required_fields([
    q1_bmis, q2_bmis, q3_bmis, q4_bmis, q5_bmis, q6_bmis, q7_bmis, q8_bmis,
    q9_bmis, q10_bmis, q11_bmis, q12_bmis, q13_bmis, q14_bmis, q15_bmis, q16_bmis
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
