import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide")

# Add progress bar (example value, adjust as needed)
st.markdown("### Πρόοδος ερωτηματολογίου")
st.progress(0.35)  # Replace 0.35 with appropriate completion %


# ΔΗΜΟΓΡΑΦΙΚΑ
st.title("Ερωτηματολόγιο")  # Survey title
st.markdown("## Δημογραφικά Στοιχεία")

age = st.number_input("Ηλικία", min_value=17, max_value=80, step=1, format="%d", value=None, placeholder="Πληκτρολογήστε την ηλικία σας")
gender = st.selectbox("Φύλο",["", "Γυναίκα", "Άντρας", "Μη-δυαδικό", "Προτιμώ να μην πω"])

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

# GOLD-MSI
# ΕΝΕΡΓΟΣ ΕΝΑΣΧΟΛΗΣΗ
st.markdown("## Ενεργός ενασχόληση με τη μουσική")
st.markdown("**Παρακαλώ επιλέξτε αυτό που σας ταιριάζει περισσότερο.**")

likert_options = ["Συμφωνώ απόλυτα", "Συμφωνώ πολύ", "Συμφωνώ", "Ούτε συμφωνώ ούτε διαφωνώ",
    "Διαφωνώ", "Διαφωνώ πολύ", "Διαφωνώ απόλυτα"]

q1_goldmsi_ae = st.radio("Περνάω πολύ από τον ελεύθερο χρόνο μου σε δραστηριότητες που σχετίζονται με τη μουσική.", likert_options, index=None, key="q1_goldmsi_ae", horizontal=True)
q2_goldmsi_ae = st.radio("Μου αρέσει να γράφω για τη μουσική, για παράδειγμα σε blog και φόρουμ.", likert_options, index=None, key="q2_goldmsi_ae", horizontal=True)
q3_goldmsi_ae = st.radio("Με ενθουσιάζουν μουσικά είδη που δεν μου είναι οικεία και θέλω να ανακαλύψω περισσότερα γι’αυτά.", likert_options, index=None, key="q3_goldmsi_ae", horizontal=True)
q4_goldmsi_ae = st.radio("Συχνά διαβάζω ή ψάχνω στο διαδίκτυο για πράγματα που σχετίζονται με τη μουσική.", likert_options, index=None, key="q4_goldmsi_ae", horizontal=True)
q5_goldmsi_ae = st.radio("Δεν ξοδεύω μεγάλο μέρος του διαθέσιμου εισοδήματός μου για τη μουσική.", likert_options, index=None, key="q5_goldmsi_ae", horizontal=True)
q6_goldmsi_ae = st.radio("Η μουσική είναι σαν εθισμός για μένα – δεν θα μπορούσα να ζήσω χωρίς αυτή.", likert_options, index=None, key="q6_goldmsi_ae", horizontal=True)
q7_goldmsi_ae = st.radio("Παρακολουθώ την καινούργια μουσική που συναντώ (π.χ. νέους καλλιτέχνες ή ηχογραφήσεις).", likert_options, index=None, key="q7_goldmsi_ae", horizontal=True)
q8_goldmsi_ae = st.radio("Έχω παρακολουθήσει __ ζωντανές μουσικές εκδηλώσεις ως ακροατής τους τελευταίους δώδεκα μήνες.", ["0", "1", "2", "3", "4-6", "7-10", "11 ή περισσότερες"], index=None, key="q8_goldmsi_ae", horizontal=True)
q9_goldmsi_ae = st.radio("Ακούω με προσοχή μουσική __ την ημέρα.", ["0-15 λεπτά", "15-30 λεπτά", "30-60 λεπτά", "60-90 λεπτά", "2 ώρες", "2-3 ώρες", "4 ώρες ή περισσότερο"], index=None, key="q9_goldmsi_ae", horizontal=True)

st.markdown("## Μουσική εκπαίδευση")

q1_goldmsi_mt = st.radio("Ποτέ δεν έχω λάβει κοπλιμέντα για τα ταλέντα μου ως μουσικός ερμηνευτής.", likert_options, index=None, key="q1_goldmsi_mt", horizontal=True)
q2_goldmsi_mt = st.radio("Δεν θα θεωρούσα τον εαυτό μου μουσικό.", likert_options, index=None, key="q2_goldmsi_mt", horizontal=True)
q3_goldmsi_mt = st.radio("Έκανα τακτική, καθημερινή εξάσκηση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) για ___ χρόνια.", ["0", "1", "2", "3", "4-5", "6-9", "10 ή περισσότερα"], index=None, horizontal=True, key="q3_goldmsi_mt")
q4_goldmsi_mt = st.radio("Στο αποκορύφωμα του ενδιαφέροντός μου, μελετούσα ___ ώρες την ημέρα το κύριο όργανό μου.", ["0", "0,5", "1", "1,5", "2", "3-4", "5 ή περισσότερες"], index=None, horizontal=True, key="q4_goldmsi_mt")
q5_goldmsi_mt = st.radio("Έχω λάβει επίσημα μαθήματα θεωρίας της μουσικής __ χρόνια.", ["0", "0,5", "1", "2", "3", "4-6", "7 ή περισσότερα"], index=None, horizontal=True, key="q5_goldmsi_mt")
q6_goldmsi_mt = st.radio("Έχω λάβει __ χρόνια επίσημη εκπαίδευση σε ένα μουσικό όργανο (συμπεριλαμβανομένης της φωνής) κατά τη διάρκεια της ζωής μου.", ["0", "0,5", "1", "2", "3-5", "6-9", "10 ή περισσότερα"], index=None, horizontal=True, key="q6_goldmsi_mt")
q7_goldmsi_mt = st.radio("Μπορώ να παίξω ___ μουσικά όργανα.", ["0", "1", "2", "3", "4", "5", "6 ή περισσότερα"], index=None, horizontal=True, key="q7_goldmsi_mt")

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

st.markdown("---")


# HSP
st.markdown("## Ευαισθησία στο Περιβάλλον")
st.markdown("**Απαντήστε σε κάθε ερώτηση σύμφωνα με τον τρόπο που προσωπικά αισθάνεστε, χρησιμοποιώντας την ακόλουθη κλίμακα:**")
st.markdown("**1 = Καθόλου  4 = Μέτρια  7 = Πάρα πολύ**")

hsp_scale = ["1", "2", "3", "4", "5", "6", "7"]

q1_hsp = st.radio("Φαίνεται να έχετε επίγνωση των λεπτομερειών στο περιβάλλον σας;", hsp_scale, index=None, key="q1_sensitivity", horizontal=True)
q2_hsp = st.radio("Καταβάλλεστε εύκολα από πράγματα όπως έντονα φώτα, δυνατές μυρωδιές, τραχιά υφάσματα ή σειρήνες κοντά σας;", hsp_scale, index=None, key="q2_sensitivity", horizontal=True)
q3_hsp = st.radio("Έχετε μια πλούσια, πολύπλοκη εσωτερική ζωή;", hsp_scale, index=None, key="q3_sensitivity", horizontal=True)
q4_hsp = st.radio("Νιώθετε αναστατωμένος/η όταν έχετε πολλά να κάνετε σε σύντομο χρονικό διάστημα;", hsp_scale, index=None, key="q4_sensitivity", horizontal=True)
q5_hsp = st.radio("Σας συγκινούν βαθιά οι τέχνες ή η μουσική;", hsp_scale, index=None, key="q5_sensitivity", horizontal=True)
q6_hsp = st.radio("Εκνευρίζεστε όταν οι άνθρωποι προσπαθούν να σας κάνουν να κάνετε πάρα πολλά πράγματα ταυτόχρονα;", hsp_scale, index=None, key="q6_sensitivity", horizontal=True)
q7_hsp = st.radio("Αποφεύγετε σκόπιμα τις βίαιες ταινίες και τηλεοπτικές εκπομπές;", hsp_scale, index=None, key="q7_sensitivity", horizontal=True)
q8_hsp = st.radio("Σας είναι δυσάρεστο να συμβαίνουν πολλά πράγματα ταυτόχρονα;", hsp_scale, index=None, key="q8_sensitivity", horizontal=True)
q9_hsp = st.radio("Οι αλλαγές στη ζωή σας σάς αναστατώνουν;", hsp_scale, index=None, key="q9_sensitivity", horizontal=True)
q10_hsp = st.radio("Παρατηρείτε και απολαμβάνετε λεπτές ή εκλεκτές μυρωδιές, γεύσεις, ήχους, έργα τέχνης;", hsp_scale, index=None, key="q10_sensitivity", horizontal=True)
q11_hsp = st.radio("Σας ενοχλούν έντονα ερεθίσματα, όπως δυνατοί θόρυβοι ή χαοτικές σκηνές;", hsp_scale, index=None, key="q11_sensitivity", horizontal=True)
q12_hsp = st.radio("Όταν πρέπει να ανταγωνιστείτε ή να σας παρατηρούν ενώ εκτελείτε μια εργασία, γίνεστε τόσο νευρικός/ή ή τρέμετε με αποτέλεσμα να αποδίδετε πολύ χειρότερα από ό,τι θα κάνατε διαφορετικά;", hsp_scale, index=None, key="q12_sensitivity", horizontal=True)

st.markdown("**1 = Καθόλου  4 = Μέτρια  7 = Πάρα πολύ**")

st.markdown("---")

# IRI
st.markdown("## Διαπροσωπική Ανταπόκριση")
st.markdown("**Για κάθε δήλωση, προσδιορίστε πόσο καλά σας χαρακτηρίζει:**")
st.markdown("**A = ΔΕΝ ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΚΑΘΟΛΟΥ  E = ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΠΟΛΥ**")

iri_options = ["Α", "Β", "Γ", "Δ", "Ε"]

q1_iri = st.radio("1. Συχνά ονειροπολώ και φαντάζομαι πράγματα που μπορεί να μου συμβούν", iri_options, index=None, key="q1_iri", horizontal=True)
q2_iri = st.radio("2. Συχνά νιώθω τρυφερότητα και νοιάζομαι για ανθρώπους λιγότερο τυχερούς από μένα", iri_options, index=None, key="q2_iri", horizontal=True)
q3_iri = st.radio("3. Μερικές φορές δυσκολεύομαι να δω τα πράγματα από την πλευρά του άλλου", iri_options, index=None, key="q3_iri", horizontal=True)
q4_iri = st.radio("4. Μερικές φορές δεν αισθάνομαι πολύ συμπονετικά για τους άλλους όταν αντιμετωπίζουν προβλήματα", iri_options, index=None, key="q4_iri", horizontal=True)
q5_iri = st.radio("5. Εντρυφώ πραγματικά στα συναισθήματα των προσώπων ενός μυθιστορήματος", iri_options, index=None, key="q5_iri", horizontal=True)
q7_iri = st.radio("7. Συνήθως προσπαθώ να είμαι αντικειμενικός/η όταν παρακολουθώ ένα κινηματογραφικό ή ένα θεατρικό έργο και δεν παρασύρομαι από αυτό", iri_options, index=None, key="q7_iri", horizontal=True)
q8_iri = st.radio("8. Σε μια διαφωνία προσπαθώ να εξετάσω όλες τις πλευρές πριν πάρω κάποια απόφαση", iri_options, index=None, key="q8_iri", horizontal=True)
q9_iri = st.radio("9. Όταν βλέπω κάποιον να τον εκμεταλλεύονται, νιώθω κάπως προστατευτικά απέναντί του", iri_options, index=None, key="q9_iri", horizontal=True)
q11_iri = st.radio("11. Μερικές φορές προσπαθώ να καταλάβω τους φίλους μου καλύτερα με το να φαντάζομαι πως βλέπουν τα πράγματα από τη δική τους σκοπιά", iri_options, index=None, key="q11_iri", horizontal=True)
q12_iri = st.radio("12. Είναι σπάνιες οι φορές που με απορροφά ένα καλό βιβλίο ή έργο", iri_options, index=None, key="q12_iri", horizontal=True)
q14_iri = st.radio("14. Οι κακοτυχίες των άλλων δεν με προβληματίζουν ιδιαίτερα", iri_options, index=None, key="q14_iri", horizontal=True)
q15_iri = st.radio("15. Εάν είμαι βέβαιος/η ότι έχω δίκιο σε κάτι, δεν χάνω το χρόνο μου ακούγοντας τα επιχειρήματα των άλλων", iri_options, index=None, key="q15_iri", horizontal=True)
q16_iri = st.radio("16. Μετά από ένα θεατρικό έργο ή μια ταινία αισθάνομαι σαν να ήμουν ένας από τους πρωταγωνιστές", iri_options, index=None, key="q16_iri", horizontal=True)
q18_iri = st.radio("18. Όταν βλέπω να φέρονται σε κάποιον άδικα, δεν συμπάσχω συχνά μαζί του", iri_options, index=None, key="q18_iri", horizontal=True)
q20_iri = st.radio("20. Συχνά επηρεάζομαι από πράγματα που βλέπω να συμβαίνουν", iri_options, index=None, key="q20_iri", horizontal=True)
q21_iri = st.radio("21. Πιστεύω ότι σε κάθε κατάσταση υπάρχουν δύο πλευρές και προσπαθώ να εξετάσω και τις δύο", iri_options, index=None, key="q21_iri", horizontal=True)
q22_iri = st.radio("22. Θα περιέγραφα τον εαυτό μου ως αρκετά συμπονετικό πρόσωπο", iri_options, index=None, key="q22_iri", horizontal=True)
q23_iri = st.radio("23. Όταν βλέπω ένα καλό έργο ταυτίζομαι εύκολα με τον πρωταγωνιστή", iri_options, index=None, key="q23_iri", horizontal=True)
q25_iri = st.radio("25. Όταν είμαι θυμωμένος/η με κάποιον προσπαθώ να ‘δω μέσα από τα μάτια του’ για λίγο", iri_options, index=None, key="q25_iri", horizontal=True)
q26_iri = st.radio("26. Όταν διαβάζω μια ενδιαφέρουσα ιστορία προσπαθώ να φανταστώ πως θα αισθανόμουν αν τα γεγονότα της ιστορίας συνέβαιναν σε μένα", iri_options, index=None, key="q26_iri", horizontal=True)
q28_iri = st.radio("28. Πριν κριτικάρω κάποιον προσπαθώ να φανταστώ πως θα αισθανόμουν εγώ στη θέση του", iri_options, index=None, key="q28_iri", horizontal=True)

st.markdown("**A = ΔΕΝ ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΚΑΘΟΛΟΥ  E = ΜΕ ΧΑΡΑΚΤΗΡΙΖΕΙ ΠΟΛΥ**")

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

st.markdown("---")
