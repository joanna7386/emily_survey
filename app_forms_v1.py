import streamlit as st
import pandas as pd
from datetime import datetime

import streamlit as st

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

