import pandas as pd
import streamlit as st
import plotly.express as px

# Charger les données
url = "https://www.data.gouv.fr/fr/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
data = pd.read_csv(url, delimiter=";")

# Configuration de la page
st.set_page_config(page_title="Dashboard des formations", layout="wide")

# Titre
st.title("Dashboard des formations")

# Analyse descriptives
st.header("Analyse descriptives")

# Répartition des candidats par sexe
sex_count = data["sexe"].value_counts()
st.subheader("Répartition des candidats par sexe")
st.bar_chart(sex_count)

# Répartition des candidats par série de baccalauréat
bac_count = data["serie_bac"].value_counts()
st.subheader("Répartition des candidats par série de baccalauréat")
st.bar_chart(bac_count)

# Ajoutez d'autres graphiques similaires pour les autres variables

# Analyse des tendances
st.header("Analyse des tendances")

# Identifier les formations et les établissements les plus demandés et les plus sélectifs
top_demand = data["formation"].value_counts().head(10)
st.subheader("Formations les plus demandées")
st.bar_chart(top_demand)

# Ajoutez d'autres graphiques et analyses pour les tendances

# Analyse des corrélations
st.header("Analyse des corrélations")

# Étudier les relations entre les caractéristiques des candidats et leur succès
correlation_matrix = data.corr()
st.subheader("Matrice de corrélation")
st.write(correlation_matrix)

# Analyse géographique
st.header("Analyse géographique")

# Cartographier la distribution des vœux et des propositions d'admission par région
region_count = data["region"].value_counts()
st.subheader("Distribution des vœux par région")
st.bar_chart(region_count)

# Analyse comparative
st.header("Analyse comparative")

# Comparer les résultats entre différentes catégories de candidats
neobac_count = data[data["categorie"] == "neo_bachelier"]["formation"].value_counts().head(10)
st.subheader("Top 10 des formations pour les néo-bacheliers")
st.bar_chart(neobac_count)

# Ajoutez d'autres graphiques pour les autres catégories de candidats et formations

# N'oubliez pas d'ajouter les bibliothèques nécessaires au début du fichier
