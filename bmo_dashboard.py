import streamlit as st
import pandas as pd
import zipfile
import requests
from io import BytesIO
import plotly.express as px

def load_data():
    url = "https://www.pole-emploi.org/files/live/sites/peorg/files/documents/Statistiques-et-analyses/Open-data/BMO/Donnees_consolidees_2022.zip"
    response = requests.get(url)

    with zipfile.ZipFile(BytesIO(response.content), "r") as zip_ref:
        xlsx_files = [f for f in zip_ref.filelist if f.filename.endswith(".xlsx")]
        with zip_ref.open(xlsx_files[0], "r") as file:
            df = pd.read_excel(file, engine="openpyxl", sheet_name=0, header=0)
    
    return df

@st.cache
def get_departments(df):
    dept_col = [col for col in df.columns if 'Dept' in col][0]
    return df[dept_col].unique()

df = load_data()

# Affiche les noms de colonnes sur le tableau de bord Streamlit
st.write(df.columns)
# Affiche les premières lignes du DataFrame sur le tableau de bord Streamlit
st.write(df.head())

departments = get_departments(df)

st.title("Dashboard Enquête Besoins en Main d'Oeuvre (BMO)")

selected_dept = st.selectbox("Sélectionnez un département", departments)

filtered_df = df[df["NomDept"] == selected_dept]

fig = px.bar(
    filtered_df, x="Nom métier BMO", y="BE22",
    title=f"Besoins en Main d'Oeuvre par métier pour le département {selected_dept}",
)
fig.update_xaxes(categoryorder="total descending")
st.plotly_chart(fig)
