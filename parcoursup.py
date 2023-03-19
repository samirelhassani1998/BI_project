import pandas as pd
import streamlit as st

# Charger les données
url = "https://www.data.gouv.fr/fr/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
data = pd.read_csv(url, delimiter=";")

# Configuration de la page
st.set_page_config(page_title="Dashboard des formations", layout="wide")

# Titre
st.title("Dashboard des formations")

# Afficher les données sous forme de tableau
st.write(data)
