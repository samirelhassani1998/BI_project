import streamlit as st
import pandas as pd
import plotly.express as px

# Chargez les données depuis l'URL
url = "https://www.data.gouv.fr/fr/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
data = pd.read_csv(url, sep=';')

# Titre du tableau de bord
st.title("Analyse des données Parcoursup")

# Répartition des candidats par sexe et série de baccalauréat
st.header("Répartition des candidats par sexe et série de baccalauréat")
fig = px.histogram(data, x="serie_bac", color="sexe", barmode="group")
st.plotly_chart(fig)

# Répartition des candidatures et des admissions par région, académie, département et type de formation (sélective ou non)
st.header("Répartition des candidatures et des admissions")
# Répartition par région
fig1 = px.histogram(data, x="reg_ins", color="statut", barmode="group")
st.plotly_chart(fig1)
# Répartition par académie
fig2 = px.histogram(data, x="aca_ins", color="statut", barmode="group")
st.plotly_chart(fig2)
# Répartition par département
fig3 = px.histogram(data, x="dep_ins", color="statut", barmode="group")
st.plotly_chart(fig3)
# Répartition par type de formation
fig4 = px.histogram(data, x="select_form", color="statut", barmode="group")
st.plotly_chart(fig4)

# Visualisation des taux d'accès par formation
st.header("Visualisation des taux d'accès")
# Taux d'accès par formation
taux_acces = data.groupby("lib_for_voe_ins")["taux_acces"].mean().reset_index()
fig5 = px.bar(taux_acces, x="lib_for_voe_ins", y="taux_acces", title="Taux d'accès par formation")
st.plotly_chart(fig5)

# Analyse des caractéristiques des candidats admis
st.header("Analyse des caractéristiques des candidats admis")
# Répartition par sexe
fig6 = px.histogram(data, x="sexe", color="statut", barmode="group")
st.plotly_chart(fig6)
# Répartition par série de baccalauréat
fig7 = px.histogram(data, x="serie_bac", color="statut", barmode="group")
st.plotly_chart(fig7)
# Répartition par mention au baccalauréat
fig8 = px.histogram(data, x="men_bac", color="statut", barmode="group")
st.plotly_chart(fig8)
# Répartition par origine géographique
fig9 = px.histogram(data, x="dep_naiss", color="statut", barmode="group")
st.plotly_chart(fig9)
# Répartition par statut de boursier
fig10 = px.histogram(data, x="boursier", color="statut", barmode="group")
st.plotly_chart(fig10)

# Analyse de la capacité d'accueil
st.header("Analyse de la capacité d'accueil")
