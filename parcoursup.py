import pandas as pd
import streamlit as st

# Charger les données
@st.cache
def load_data():
    data_url = 'https://www.data.gouv.fr/fr/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db'
    df = pd.read_csv(data_url, delimiter=';', encoding='utf-8', low_memory=False)
    return df

df = load_data()

# Afficher les données
st.title("Données sur les admissions Parcoursup")
st.write(df)
