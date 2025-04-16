import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

st.title("Ερωτηματολόγιο")  # Survey title
st.markdown("## Δημογραφικά Στοιχεία")

# Ηλικία (numeric input)
age = st.number_input("Ηλικία", min_value=17, max_value=80, step=1, format="%d", value=None, placeholder="Πληκτρολογήστε την ηλικία σας")

gender = st.selectbox(
    "Φύλο",
    ["", "Γυναίκα", "Άντρας", "Μη-δυαδικό", "Προτιμώ να μην πω"]
)

st.markdown("## Ενασχόληση με τη Μουσική")

st.text_input("Το μουσικό όργανο που παίζω καλύτερα (συμπεριλαμβανομένης της φωνής) είναι:", placeholder="π.χ. πιάνο, κιθάρα, φλάουτο, φωνή", key="instrument_goldmsi")

genre_listen_options = ["Ροκ/ποπ", "Τζαζ", "Κλασική", "Ελληνική παραδοσιακή", "Άλλο"]

q1_music_style = st.radio("Ποιο είναι το μουσικό είδος που ακούτε κυρίως;", genre_listen_options, index=None, key="q1_music_style")

if q1_music_style == "Άλλο":
    q1_music_style_other = st.text_input("Παρακαλώ διευκρινίστε:", key="q1_music_style_other")
else:
    q1_music_style_other = ""

genre_training_options = ["Ροκ/ποπ", "Τζαζ", "Κλασική", "Ελληνική παραδοσιακή", "Άλλο", "Καμία"]

q2_music_training = st.radio("Σε ποιο μουσικό είδος έχετε εκπαιδευτεί;", genre_training_options, index=None, key="q2_music_training")

if q2_music_training == "Άλλο":
    q2_music_training_other = st.text_input("Παρακαλώ διευκρινίστε:", key="q2_music_training_other")
else:
    q2_music_training_other = ""


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

q1_goldmsi = st.radio("Περνάω πολύ από τον ελεύθερο χρόνο μου σε δραστηριότητες που σχετίζονται με τη μουσική.", likert_options, index=None, key="q1_goldmsi")
q2_goldmsi = st.radio("Μου αρέσει να γράφω για τη μουσική, για παράδειγμα σε blog και φόρουμ.", likert_options, index=None, key="q2_goldmsi")
q3_goldmsi = st.radio("Με ενθουσιάζουν μουσικά είδη που δεν μου είναι οικεία και θέλω να ανακαλύψω περισσότερα γι’αυτά.", likert_options, index=None, key="q3_goldmsi")
q4_goldmsi = st.radio("Συχνά διαβάζω ή ψάχνω στο διαδίκτυο για πράγματα που σχετίζονται με τη μουσική.", likert_options, index=None, key="q4_goldmsi")
q5_goldmsi = st.radio("Δεν ξοδεύω μεγάλο μέρος του διαθέσιμου εισοδήματός μου για τη μουσική.", likert_options, index=None, key="q5_goldmsi")
q6_goldmsi = st.radio("Η μουσική είναι σαν εθισμός για μένα – δεν θα μπορούσα να ζήσω χωρίς αυτή.", likert_options, index=None, key="q6_goldmsi")
q7_goldmsi = st.radio("Παρακολουθώ την καινούργια μουσική που συναντώ (π.χ. νέους καλλιτέχνες ή ηχογραφήσεις).", likert_options, index=None, key="q7_goldmsi")

st.markdown("## Μουσική Εμπειρία")

q8_goldmsi = st.radio("Έχω παρακολουθήσει __ ζωντανές μουσικές εκδηλώσεις ως ακροατής τους τελευταίους δώδεκα μήνες.", ["0", "1", "2", "3", "4-6", "7-10", "11+"], index=None, key="q8_goldmsi")
q9_goldmsi = st.radio("Ακούω μουσική με προσοχή __ την ημέρα.", ["0-15 λεπτά", "15-30 λεπτά", "30-60 λεπτά", "60-90 λεπτά", "2 ώρες", "2-3 ώρες", "4 ώρες ή περισσότερο"], index=None, key="q9_goldmsi")

st.markdown("## Μουσική Ταυτότητα / Αυτοαντίληψη")

q10_goldmsi = st.radio("Ποτέ δεν έχω λάβει κοπλιμέντα για τα ταλέντα μου ως μουσικός ερμηνευτής.", likert_options, index=None, key="q10_goldmsi")
q11_goldmsi = st.radio("Δεν θα θεωρούσα τον εαυτό μου μουσικό.", likert_options, index=None, key="q11_goldmsi")
q12_goldmsi = st.radio("Στο αποκορύφωμα του ενδιαφέροντός μου, μελετούσα ___ ώρες την ημέρα το κύριο όργανό μου.", ["0", "0,5", "1", "1,5", "2", "3-4", "5 ή περισσότερες"], index=None, key="q12_goldmsi")
q13_goldmsi = st.radio("Έχω λάβει επίσημα μαθήματα θεωρίας της μουσικής __ χρόνια.", ["0", "0,5", "1", "2", "3", "4-6", "7 ή περισσότερα"], index=None, key="q13_goldmsi")
q14_goldmsi = st.radio("Έχω λάβει __ χρόνια επίσημη εκπαίδευση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) κατά τη διάρκεια της ζωής μου.", ["0", "0,5", "1", "2", "3-5", "6-9", "10 ή περισσότερα"], index=None, key="q14_goldmsi")
q15_goldmsi = st.radio("Μπορώ να παίξω ___ μουσικά όργανα.", ["0", "1", "2", "3", "4", "5", "6 ή περισσότερα"], index=None, key="q15_goldmsi")


st.markdown("## Συναισθηματική Αντίδραση στη Μουσική")

q16_goldmsi = st.radio("Κάποιες φορές επιλέγω μουσική που μπορεί να με κάνει να ανατριχιάσω.", likert_options, index=None, key="q16_goldmsi")
q17_goldmsi = st.radio("Σπάνια τα μουσικά κομμάτια μου προκαλούν συναισθήματα.", likert_options, index=None, key="q17_goldmsi")
q18_goldmsi = st.radio("Συχνά επιλέγω συγκεκριμένη μουσική για να με παρακινήσει ή να με ενθουσιάσει.", likert_options, index=None, key="q18_goldmsi")
q19_goldmsi = st.radio("Μπορώ να προσδιορίσω τι είναι ιδιαίτερο σε ένα συγκεκριμένο μουσικό κομμάτι.", likert_options, index=None, key="q19_goldmsi")
q20_goldmsi = st.radio("Μπορώ να μιλήσω για τα συναισθήματα που μου προκαλεί ένα μουσικό κομμάτι.", likert_options, index=None, key="q20_goldmsi")
q21_goldmsi = st.radio("Η μουσική μπορεί να μου ανακαλέσει αναμνήσεις από ανθρώπους και μέρη του παρελθόντος.", likert_options, index=None, key="q21_goldmsi")


st.markdown("## Προσωπικότητα")
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

q1_tipi = st.radio("Εξωστρεφή, ενθουσιώδη", tipi_options, index=None, key="q1_tipi")
q2_tipi = st.radio("Επικριτικό, εριστικό", tipi_options, index=None, key="q2_tipi")
q3_tipi = st.radio("Αξιόπιστο, πειθαρχημένο", tipi_options, index=None, key="q3_tipi")
q4_tipi = st.radio("Αγχώδη, αναστατώνεται εύκολα", tipi_options, index=None, key="q4_tipi")
q5_tipi = st.radio("Ανοιχτό σε νέες εμπειρίες, περίπλοκο", tipi_options, index=None, key="q5_tipi")
q6_tipi = st.radio("Συγκρατημένο, ήσυχο", tipi_options, index=None, key="q6_tipi")
q7_tipi = st.radio("Συμπαθητικό, ζεστό", tipi_options, index=None, key="q7_tipi")
q8_tipi = st.radio("Ανοργάνωτο, απρόσεκτο", tipi_options, index=None, key="q8_tipi")
q9_tipi = st.radio("Ήρεμο, συναισθηματικά σταθερό", tipi_options, index=None, key="q9_tipi")
q10_tipi = st.radio("Συμβατικό, μη δημιουργικό", tipi_options, index=None, key="q10_tipi")


st.markdown("## Νοοτροπία για τη Δημιουργικότητα")
st.markdown("Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.")

cms_options = [
    "1  Σίγουρα όχι",
    "2", "3", "4",
    "5  Σίγουρα ναι"
]

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


st.markdown("## Διάθεση")
st.markdown("Διαλέξτε την απάντηση στην παρακάτω κλίμακα που δείχνει πόσο καλά κάθε επίθετο ή φράση περιγράφει την παρούσα διάθεσή σας.")

bmis_options = [
    "1  Σίγουρα δεν νιώθω",
    "2", "3", "4", "5", "6",
    "7  Σίγουρα νιώθω"
]

q1_bmis = st.radio("Ζωηρός", bmis_options, index=None, key="q1_mood", horizontal=True)
q2_bmis = st.radio("Χαρούμενος", bmis_options, index=None, key="q2_mood", horizontal=True)
q3_bmis = st.radio("Λυπημένος", bmis_options, index=None, key="q3_mood", horizontal=True)
q4_bmis = st.radio("Κουρασμένος", bmis_options, index=None, key="q4_mood", horizontal=True)
q5_bmis = st.radio("Caring", bmis_options, index=None, key="q5_mood", horizontal=True)
q6_bmis = st.radio("Ευχαριστημένος (Content)", bmis_options, index=None, key="q6_mood", horizontal=True)
q7_bmis = st.radio("Κακόκεφος (Gloomy)", bmis_options, index=None, key="q7_mood", horizontal=True)
q8_bmis = st.radio("Νευρικός", bmis_options, index=None, key="q8_mood", horizontal=True)
q9_bmis = st.radio("Νυσταγμένος", bmis_options, index=None, key="q9_mood", horizontal=True)
q10_bmis = st.radio("Γκρινιάρης", bmis_options, index=None, key="q10_mood", horizontal=True)
q11_bmis = st.radio("Ζωηρός (peppy)", bmis_options, index=None, key="q11_mood", horizontal=True)
q12_bmis = st.radio("Αγχωμένος", bmis_options, index=None, key="q12_mood", horizontal=True)
q13_bmis = st.radio("Ήρεμος", bmis_options, index=None, key="q13_mood", horizontal=True)
q14_bmis = st.radio("Τρυφερός (loving)", bmis_options, index=None, key="q14_mood", horizontal=True)
q15_bmis = st.radio("Fed up", bmis_options, index=None, key="q15_mood", horizontal=True)
q16_bmis = st.radio("Δραστήριος", bmis_options, index=None, key="q16_mood", horizontal=True)


st.markdown("## Κλίμακα Ευαισθησίας στο Περιβάλλον")
st.markdown("Απαντήστε σε κάθε ερώτηση σύμφωνα με τον τρόπο που προσωπικά αισθάνεστε, χρησιμοποιώντας την ακόλουθη κλίμακα:")
st.markdown("**1 = Καθόλου  4 = Μέτρια  7 = Πάρα πολύ**")

hsp_scale = ["1", "2", "3", "4", "5", "6", "7"]

q1_hsp = st.radio("1. Φαίνεται να έχετε επίγνωση των λεπτομερειών στο περιβάλλον σας;", hsp_scale, index=None, key="q1_sensitivity")
q2_hsp = st.radio("2. Καταβάλλεστε εύκολα από πράγματα όπως έντονα φώτα, δυνατές μυρωδιές, τραχιά υφάσματα ή σειρήνες κοντά σας;", hsp_scale, index=None, key="q2_sensitivity")
q3_hsp = st.radio("3. Έχετε μια πλούσια, πολύπλοκη εσωτερική ζωή;", hsp_scale, index=None, key="q3_sensitivity")
q4_hsp = st.radio("4. Νιώθετε αναστατωμένος/η όταν έχετε πολλά να κάνετε σε σύντομο χρονικό διάστημα;", hsp_scale, index=None, key="q4_sensitivity")
q5_hsp = st.radio("5. Σας συγκινούν βαθιά οι τέχνες ή η μουσική;", hsp_scale, index=None, key="q5_sensitivity")
q6_hsp = st.radio("6. Εκνευρίζεστε όταν οι άνθρωποι προσπαθούν να σας κάνουν να κάνετε πάρα πολλά πράγματα ταυτόχρονα;", hsp_scale, index=None, key="q6_sensitivity")
q7_hsp = st.radio("7. Αποφεύγετε σκόπιμα τις βίαιες ταινίες και τηλεοπτικές εκπομπές;", hsp_scale, index=None, key="q7_sensitivity")
q8_hsp = st.radio("8. Σας είναι δυσάρεστο να συμβαίνουν πολλά πράγματα ταυτόχρονα;", hsp_scale, index=None, key="q8_sensitivity")
q9_hsp = st.radio("9. Οι αλλαγές στη ζωή σας σάς αναστατώνουν;", hsp_scale, index=None, key="q9_sensitivity")
q10_hsp = st.radio("10. Παρατηρείτε και απολαμβάνετε λεπτές ή εκλεκτές μυρωδιές, γεύσεις, ήχους, έργα τέχνης;", hsp_scale, index=None, key="q10_sensitivity")
q11_hsp = st.radio("11. Σας ενοχλούν έντονα ερεθίσματα, όπως δυνατοί θόρυβοι ή χαοτικές σκηνές;", hsp_scale, index=None, key="q11_sensitivity")
q12_hsp = st.radio("12. Όταν πρέπει να ανταγωνιστείτε ή να σας παρατηρούν ενώ εκτελείτε μια εργασία, γίνεστε τόσο νευρικός/ή ή τρέμετε με αποτέλεσμα να αποδίδετε πολύ χειρότερα από ό,τι θα κάνατε διαφορετικά;", hsp_scale, index=None, key="q12_sensitivity")


st.markdown("## Κλίμακα Διαπροσωπικής Ανταπόκρισης (IRI)")
st.markdown("Για κάθε δήλωση, προσδιορίστε πόσο καλά σας περιγράφει:")

iri_options = [
    "Α  ΔΕΝ ΜΕ ΠΕΡΙΓΡΑΦΕΙ ΚΑΘΟΛΟΥ",
    "Β",
    "Γ",
    "Δ",
    "Ε  ΜΕ ΠΕΡΙΓΡΑΦΕΙ ΠΟΛΥ ΚΑΛΑ"
]

q1_iri = st.radio("1. Συχνά ονειροπολώ και φαντάζομαι πράγματα που μπορεί να μου συμβούν", iri_options, index=None, key="q1_iri", horizontal=True)
q2_iri = st.radio("2. Συχνά νιώθω τρυφερότητα και νοιάζομαι για ανθρώπους λιγότερο τυχερούς από μένα", iri_options, index=None, key="q2_iri", horizontal=True)
q3_iri = st.radio("3. Μερικές φορές δυσκολεύομαι να δω τα πράγματα από την πλευρά του άλλου", iri_options, index=None, key="q3_iri", horizontal=True)
q4_iri = st.radio("4. Μερικές φορές δεν αισθάνομαι πολύ συμπονετικά για τους άλλους όταν αντιμετωπίζουν προβλήματα", iri_options, index=None, key="q4_iri", horizontal=True)
q5_iri = st.radio("5. Εντρυφώ πραγματικά στα συναισθήματα των προσώπων ενός μυθιστορήματος", iri_options, index=None, key="q5_iri", horizontal=True)
q6_iri = st.radio("6. Σε καταστάσεις έκτακτης ανάγκης αισθάνομαι αμηχανία και ανησυχία", iri_options, index=None, key="q6_iri", horizontal=True)
q7_iri = st.radio("7. Συνήθως προσπαθώ να είμαι αντικειμενικός/η όταν παρακολουθώ ένα κινηματογραφικό ή ένα θεατρικό έργο και δεν παρασύρομαι από αυτό", iri_options, index=None, key="q7_iri", horizontal=True)
q8_iri = st.radio("8. Σε μια διαφωνία προσπαθώ να εξετάσω όλες τις πλευρές πριν πάρω κάποια απόφαση", iri_options, index=None, key="q8_iri", horizontal=True)
q9_iri = st.radio("9. Όταν βλέπω κάποιον να τον εκμεταλλεύονται, νιώθω κάπως προστατευτικά απέναντί του", iri_options, index=None, key="q9_iri", horizontal=True)
q10_iri = st.radio("10. Μερικές φορές αισθάνομαι ανήμπορος/η όταν είμαι στο μέσο μιας κατάστασης με έντονη συναισθηματική φόρτιση", iri_options, index=None, key="q10_iri", horizontal=True)
q11_iri = st.radio("11. Μερικές φορές προσπαθώ να καταλάβω τους φίλους μου καλύτερα με το να φαντάζομαι πως βλέπουν τα πράγματα από τη δική τους σκοπιά", iri_options, index=None, key="q11_iri", horizontal=True)
q12_iri = st.radio("12. Είναι σπάνιες οι φορές που με απορροφά ένα καλό βιβλίο ή έργο", iri_options, index=None, key="q12_iri", horizontal=True)
q13_iri = st.radio("13. Όταν βλέπω κάποιο τραυματισμένο, προσπαθώ να παραμείνω ψύχραιμος", iri_options, index=None, key="q13_iri", horizontal=True)
q14_iri = st.radio("14. Οι κακοτυχίες των άλλων δεν με προβληματίζουν ιδιαίτερα", iri_options, index=None, key="q14_iri", horizontal=True)
q15_iri = st.radio("15. Εάν είμαι βέβαιος/η ότι έχω δίκιο σε κάτι, δεν χάνω το χρόνο μου ακούγοντας τα επιχειρήματα των άλλων", iri_options, index=None, key="q15_iri", horizontal=True)
q16_iri = st.radio("16. Μετά από ένα θεατρικό έργο ή μια ταινία αισθάνομαι σαν να ήμουν ένας από τους πρωταγωνιστές", iri_options, index=None, key="q16_iri", horizontal=True)
q17_iri = st.radio("17. Με τρομάζει να βρίσκομαι σε μια κατάσταση με έντονη συναισθηματική φόρτιση", iri_options, index=None, key="q17_iri", horizontal=True)
q18_iri = st.radio("18. Όταν βλέπω να φέρονται σε κάποιον άδικα, δεν συμπάσχω συχνά μαζί του", iri_options, index=None, key="q18_iri", horizontal=True)
q19_iri = st.radio("19. Συνήθως είμαι αρκετά αποτελεσματικός στο να ανταπεξέρχομαι τις δύσκολες καταστάσεις", iri_options, index=None, key="q19_iri", horizontal=True)
q20_iri = st.radio("20. Συχνά επηρεάζομαι από πράγματα που βλέπω να συμβαίνουν", iri_options, index=None, key="q20_iri", horizontal=True)
q21_iri = st.radio("21. Πιστεύω ότι σε κάθε κατάσταση υπάρχουν δύο πλευρές και προσπαθώ να εξετάσω και τις δύο", iri_options, index=None, key="q21_iri", horizontal=True)
q22_iri = st.radio("22. Θα περιέγραφα τον εαυτό μου ως αρκετά συμπονετικό πρόσωπο", iri_options, index=None, key="q22_iri", horizontal=True)
q23_iri = st.radio("23. Όταν βλέπω ένα καλό έργο ταυτίζομαι εύκολα με τον πρωταγωνιστή", iri_options, index=None, key="q23_iri", horizontal=True)
q24_iri = st.radio("24. Έχω την τάση να χάνω τον έλεγχό μου σε έκτακτες καταστάσεις", iri_options, index=None, key="q24_iri", horizontal=True)
q25_iri = st.radio("25. Όταν είμαι θυμωμένος/η με κάποιον προσπαθώ να ‘δω μέσα από τα μάτια του’ για λίγο", iri_options, index=None, key="q25_iri", horizontal=True)
q26_iri = st.radio("26. Όταν διαβάζω μια ενδιαφέρουσα ιστορία προσπαθώ να φανταστώ πως θα αισθανόμουν αν τα γεγονότα της ιστορίας συνέβαιναν σε μένα", iri_options, index=None, key="q26_iri", horizontal=True)
q27_iri = st.radio("27. Όταν βλέπω κάποιον που χρειάζεται άμεσα βοήθεια σε μια κρίσιμη κατάσταση, αποδιοργανώνομαι", iri_options, index=None, key="q27_iri", horizontal=True)
q28_iri = st.radio("28. Πριν κριτικάρω κάποιον προσπαθώ να φανταστώ πως θα αισθανόμουν εγώ στη θέση του", iri_options, index=None, key="q28_iri", horizontal=True)


st.markdown("## Κλίμακα Συναισθηματικής Μετάδοσης (Emotional Contagion Scale - EC)")
st.markdown("Απάντησε σύμφωνα με τον δικό σου τρόπο να σκέφτεσαι, να αισθάνεσαι και να ενεργείς σε διάφορες καταστάσεις:")

emotcont_options = [
    "1  (Ποτέ)",
    "2",
    "3",
    "4",
    "5  (Πάντα)"
]

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


