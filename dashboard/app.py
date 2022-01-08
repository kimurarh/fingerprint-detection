import streamlit as st
from pages import intro, model_training, demo

st.title("Fingerprint Detection")
st.write("___")

section = st.sidebar.radio(
    "Go to:",
    ("Intro",
     "Model",
     "Demo")
)

if section == 'Intro':
    intro()
elif section == "Model":
    model_training()
elif section == "Demo":
    demo()
