import streamlit as st
import pandas as pd
from datetime import datetime

import streamlit as st

# st.set_page_config(layout="wide")

st.title("Ερωτηματολόγιο")  # Survey title
st.markdown("## Δημογραφικά Στοιχεία")

# Ηλικία (numeric input)
age = st.number_input("Ηλικία", min_value=10, max_value=120, step=1, format="%d", value=None, placeholder="Πληκτρολογήστε την ηλικία σας")

gender = st.selectbox(
    "Φύλο",
    ["", "Γυναίκα", "Άντρας", "Μη-δυαδικό", "Προτιμώ να μην πω"]
)

st.markdown("## Δείκτης Μουσικής Δεξιότητας (Goldsmiths)")
st.markdown("Παρακαλώ επιλέξτε αυτό που ταιριάζει στην περίπτωσή σας.")

likert_options = [
    "Συμφωνώ απολύτως",
    "Συμφωνώ εντόνως",
    "Συμφωνώ",
    "Ούτε συμφωνώ ούτε διαφωνώ",
    "Διαφωνώ",
    "Διαφωνώ εντόνως",
    "Διαφωνώ πλήρως"
]

q1 = st.radio("Περνάω πολύ από τον ελεύθερο χρόνο μου σε δραστηριότητες που σχετίζονται με τη μουσική.", likert_options, index=None, key="q1")
q2 = st.radio("Μου αρέσει να γράφω για τη μουσική, για παράδειγμα σε blog και φόρουμ.", likert_options, index=None, key="q2")
q3 = st.radio("Με ιντριγκάρουν τα μουσικά στυλ που δεν γνωρίζω και θέλω να ανακαλύψω περισσότερα.", likert_options, index=None, key="q3")
q4 = st.radio("Συχνά διαβάζω ή ψάχνω στο διαδίκτυο για πράγματα που σχετίζονται με τη μουσική.", likert_options, index=None, key="q4")
q5 = st.radio("Δεν ξοδεύω μεγάλο μέρος του διαθέσιμου εισοδήματός μου στη μουσική.", likert_options, index=None, key="q5")
q6 = st.radio("Η μουσική είναι ένα είδος εθισμού για μένα - δεν θα μπορούσα να ζήσω χωρίς αυτήν.", likert_options, index=None, key="q6")
q7 = st.radio("Παρακολουθώ την καινούργια μουσική που συναντώ (π.χ. νέους καλλιτέχνες ή ηχογραφήσεις).", likert_options, index=None, key="q7")

st.markdown("## Μουσική Εμπειρία")

q8 = st.radio(
    "Έχω παρακολουθήσει __ ζωντανές μουσικές εκδηλώσεις ως κοινό τους τελευταίους δώδεκα μήνες.",
    ["0", "1", "2", "3", "4-6", "7-10", "11+"],
    index=None,
    key="q8"
)

q9 = st.radio(
    "Ακούω προσεκτικά μουσική __ την ημέρα.",
    ["0-15 λεπτά", "15-30 λεπτά", "30-60 λεπτά", "60-90 λεπτά", "2 ώρες", "2-3 ώρες", "4 ώρες ή περισσότερο"],
    index=None,
    key="q9"
)

st.markdown("## Μουσική Ταυτότητα / Αυτοαντίληψη")

likert_options = [
    "Συμφωνώ απολύτως",
    "Συμφωνώ εντόνως",
    "Συμφωνώ",
    "Ούτε συμφωνώ ούτε διαφωνώ",
    "Διαφωνώ",
    "Διαφωνώ εντόνως",
    "Διαφωνώ πλήρως"
]

q10 = st.radio(
    "Ποτέ δεν έχω λάβει κοπλιμέντα για τα ταλέντα μου ως μουσικός ερμηνευτής.",
    likert_options,
    index=None,
    key="q10"
)

q11 = st.radio(
    "Δεν θα θεωρούσα τον εαυτό μου μουσικό.",
    likert_options,
    index=None,
    key="q11"
)

q12 = st.radio(
    "Στο αποκορύφωμα της μελέτης μου, μελετούσα ___ ώρες την ημέρα στο κύριο όργανό μου.",
    ["0", "0,5", "1", "1,5", "2", "3-4", "5 ή περισσότερες"],
    index=None,
    key="q12"
)

q13 = st.radio(
    "Έχω κάνει τυπικά μαθήματα θεωρίας της μουσικής __ χρόνια.",
    ["0", "0,5", "1", "2", "3", "4-6", "7 ή περισσότερα"],
    index=None,
    key="q13"
)

q14 = st.radio(
    "Έχω λάβει __ χρόνια τυπική εκπαίδευση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) κατά τη διάρκεια της ζωής μου.",
    ["0", "0,5", "1", "2", "3-5", "6-9", "10 ή περισσότερα"],
    index=None,
    key="q14"
)

q15 = st.radio(
    "Μπορώ να παίξω ___ μουσικά όργανα.",
    ["0", "1", "2", "3", "4", "5", "6 ή περισσότερα"],
    index=None,
    key="q15"
)

st.markdown("## Συναισθηματική Αντίδραση στη Μουσική")

likert_options = [
    "Συμφωνώ απολύτως",
    "Συμφωνώ εντόνως",
    "Συμφωνώ",
    "Ούτε συμφωνώ ούτε διαφωνώ",
    "Διαφωνώ",
    "Διαφωνώ εντόνως",
    "Διαφωνώ πλήρως"
]

q16 = st.radio(
    "Κάποιες φορές επιλέγω μουσική που μπορεί να προκαλέσει ρίγη στη σπονδυλική μου στήλη.",
    likert_options,
    index=None,
    key="q16"
)

q17 = st.radio(
    "Μουσικά κομμάτια σπάνια μου προκαλούν συναισθήματα.",
    likert_options,
    index=None,
    key="q17"
)

q18 = st.radio(
    "Συχνά επιλέγω συγκεκριμένη μουσική για να με παρακινήσει ή να με συγκινήσει (EXCITE ME).",
    likert_options,
    index=None,
    key="q18"
)

q19 = st.radio(
    "Μπορώ να προσδιορίσω τι είναι ιδιαίτερο σε ένα συγκεκριμένο μουσικό κομμάτι.",
    likert_options,
    index=None,
    key="q19"
)

q20 = st.radio(
    "Μπορώ να μιλήσω για τα συναισθήματα που μου προκαλεί ένα μουσικό κομμάτι.",
    likert_options,
    index=None,
    key="q20"
)

q21 = st.radio(
    "Η μουσική μπορεί να μου ξυπνήσει αναμνήσεις από ανθρώπους και μέρη του παρελθόντος.",
    likert_options,
    index=None,
    key="q21"
)

st.markdown("## Απογραφή Προσωπικότητας 10 Στοιχείων (TIPI)")
st.markdown("**Βλέπω τον εαυτό μου ως:**")

tipi_options = [
    "Διαφωνώ απόλυτα",
    "Διαφωνώ μέτρια",
    "Διαφωνώ λίγο",
    "Δεν συμφωνώ ούτε διαφωνώ",
    "Συμφωνώ λίγο",
    "Συμφωνώ μέτρια",
    "Συμφωνώ απόλυτα"
]

q22 = st.radio("Εξωστρεφή, ενθουσιώδη", tipi_options, index=None, key="q22")
q23 = st.radio("Επικριτικό, quarrelsome", tipi_options, index=None, key="q23")
q24 = st.radio("Dependable, αυτοπειθαρχημένο", tipi_options, index=None, key="q24")
q25 = st.radio("Ανήσυχο, easily upset", tipi_options, index=None, key="q25")
q26 = st.radio("Ανοιχτό σε νέες εμπειρίες, πολύπλοκο", tipi_options, index=None, key="q26")
q27 = st.radio("Συγκρατημένο, ήσυχο", tipi_options, index=None, key="q27")
q28 = st.radio("Συμπαθητικό, ζεστό", tipi_options, index=None, key="q28")
q29 = st.radio("Ανοργάνωτο, απρόσεκτο (careless)", tipi_options, index=None, key="q29")
q30 = st.radio("Ήρεμο, συναισθηματικά σταθερό", tipi_options, index=None, key="q30")
q31 = st.radio("Συμβατικό, μη δημιουργικό", tipi_options, index=None, key="q31")

st.markdown("## Κλίμακα Δημιουργικής Νοοτροπίας")
st.markdown("Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.")

mindset_options = [
    "1  Σίγουρα όχι",
    "2", "3", "4",
    "5  Σίγουρα ναι"
]

q32 = st.radio("Ο καθένας μπορεί να δημιουργήσει κάτι σπουδαίο κάποια στιγμή, αν του/της δίνονται κατάλληλες συνθήκες", mindset_options, index=None, key="q32", horizontal=True)
q33 = st.radio("Είτε είναι κανείς δημιουργικός είτε δεν είναι—ακόμα κι να προσπαθήσει πολύ σκληρά δεν μπορεί να αλλάξει πολλά", mindset_options, index=None, key="q33", horizontal=True)
q34 = st.radio("Ο καθένας/η καθεμία μπορεί να αναπτύξει τις δημιουργικές του/της ικανότητες μέχρι ένα ορισμένο επίπεδο", mindset_options, index=None, key="q34", horizontal=True)
q35 = st.radio("Πρέπει να είσαι γεννημένος/η δημιουργός—χωρίς έμφυτο ταλέντο μπορείς μόνο να είσαι κακότεχνος", mindset_options, index=None, key="q35", horizontal=True)
q36 = st.radio("Η εξάσκηση σε τελειοποιεί—η επιμονή και η σκληρή προσπάθεια είναι οι καλύτεροι τρόποι να αναπτύξει και να επεκτείνει κάποιος/α τις δυνατότητές του/της", mindset_options, index=None, key="q36", horizontal=True)
q37 = st.radio("Η δημιουργικότητα μπορεί να αναπτυχθεί, αλλά κάποιος/α είτε είναι είτε δεν είναι ένα πραγματικά δημιουργικό άτομο", mindset_options, index=None, key="q37", horizontal=True)
q38 = st.radio("Η Ρώμη δεν χτίστηκε σε μια μέρα—η δημιουργικότητα απαιτεί προσπάθεια και δουλειά, και αυτά τα δύο είναι πιο σημαντικά από το ταλέντο", mindset_options, index=None, key="q38", horizontal=True)
q39 = st.radio("Μερικοί άνθρωποι είναι δημιουργικοί, άλλοι δεν είναι—και καμία εξάσκηση δεν μπορεί να το αλλάξει", mindset_options, index=None, key="q39", horizontal=True)
q40 = st.radio("Δεν έχει σημασία ποιο επίπεδο δημιουργικότητας επιδεικνύει κάποιος—μπορείς πάντα να το αυξήσεις", mindset_options, index=None, key="q40", horizontal=True)
q41 = st.radio("Ένα αληθινά δημιουργικό ταλέντο είναι έμφυτο και σταθερό σε ολόκληρη τη ζωή του ατόμου", mindset_options, index=None, key="q41", horizontal=True)

st.markdown("## Σύντομη Κλίμακα Ενδοσκόπησης Διάθεσης")
st.markdown("Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.")

mood_options = [
    "1  Σίγουρα δεν νιώθω",
    "2", "3", "4", "5", "6",
    "7  Σίγουρα νιώθω"
]

q42 = st.radio("Ζωηρός", mood_options, index=None, key="q42", horizontal=True)
q43 = st.radio("Χαρούμενος", mood_options, index=None, key="q43", horizontal=True)
q44 = st.radio("Λυπημένος", mood_options, index=None, key="q44", horizontal=True)
q45 = st.radio("Κουρασμένος", mood_options, index=None, key="q45", horizontal=True)
q46 = st.radio("Caring", mood_options, index=None, key="q46", horizontal=True)
q47 = st.radio("Ευχαριστημένος (Content)", mood_options, index=None, key="q47", horizontal=True)
q48 = st.radio("Κακόκεφος (Gloomy)", mood_options, index=None, key="q48", horizontal=True)
q49 = st.radio("Νευρικός", mood_options, index=None, key="q49", horizontal=True)
q50 = st.radio("Νυσταγμένος", mood_options, index=None, key="q50", horizontal=True)
q51 = st.radio("Γκρινιάρης", mood_options, index=None, key="q51", horizontal=True)
q52 = st.radio("Ζωηρός (peppy)", mood_options, index=None, key="q52", horizontal=True)
q53 = st.radio("Αγχωμένος", mood_options, index=None, key="q53", horizontal=True)
q54 = st.radio("Ήρεμος", mood_options, index=None, key="q54", horizontal=True)
q55 = st.radio("Τρυφερός (loving)", mood_options, index=None, key="q55", horizontal=True)
q56 = st.radio("Fed up", mood_options, index=None, key="q56", horizontal=True)
q57 = st.radio("Δραστήριος", mood_options, index=None, key="q57", horizontal=True)


