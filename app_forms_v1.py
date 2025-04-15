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


