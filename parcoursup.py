"""Application Streamlit pour l'analyse des admissions Parcoursup."""

from typing import Optional

import os

import pandas as pd
import streamlit as st
import plotly.express as px


DEFAULT_URL = "https://www.data.gouv.fr/fr/datasets/r/1d916b7c-bd4c-4951-845a-70f7ad7c17db"
DATA_URL = os.environ.get("DATA_URL", DEFAULT_URL)


def configure_page() -> None:
    """Configure la page Streamlit."""
    st.set_page_config(page_title="Tableau de bord Parcoursup", layout="wide")


@st.cache_data(show_spinner=True)
def load_data() -> Optional[pd.DataFrame]:
    """Charge le jeu de données depuis DATA_URL."""

    try:
        df = pd.read_csv(DATA_URL, delimiter=";", encoding="utf-8", low_memory=False)
    except Exception as exc:  # pragma: no cover - dépend du réseau
        st.error(f"Erreur lors du chargement des données: {exc}")
        return None
    return df


def sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """Applique dynamiquement des filtres via la barre latérale."""

    st.sidebar.header("Filtres")
    filtered = df.copy()

    for column in df.select_dtypes(include="object").columns:
        values = sorted(df[column].dropna().unique())
        selection = st.sidebar.multiselect(column, values)
        if selection:
            filtered = filtered[filtered[column].isin(selection)]

    for column in df.select_dtypes(include="number").columns:
        min_value, max_value = df[column].min(), df[column].max()
        selection = st.sidebar.slider(
            column,
            float(min_value),
            float(max_value),
            (float(min_value), float(max_value)),
        )
        filtered = filtered[filtered[column].between(selection[0], selection[1])]

    return filtered


def main() -> None:
    """Point d'entrée de l'application."""

    configure_page()
    st.title("Données sur les admissions Parcoursup")

    df = load_data()
    if df is None:
        return

    st.write(f"{len(df):,} lignes chargées.")

    filtered_df = sidebar_filters(df)

    st.subheader("Aperçu des données")
    st.dataframe(filtered_df.head())

    st.subheader("Statistiques descriptives")
    st.write(filtered_df.describe())

    numeric_cols = filtered_df.select_dtypes(include="number").columns
    if numeric_cols.empty:
        st.info("Aucune colonne numérique à visualiser.")
        return

    st.subheader("Visualisation")
    col1, col2, col3 = st.columns(3)
    with col1:
        x_axis = st.selectbox("Axe X", options=filtered_df.columns)
    with col2:
        y_axis = st.selectbox("Axe Y", options=numeric_cols)
    with col3:
        chart_type = st.selectbox("Type", ["Barres", "Lignes", "Scatter"])

    if chart_type == "Barres":
        fig = px.bar(filtered_df, x=x_axis, y=y_axis)
    elif chart_type == "Lignes":
        fig = px.line(filtered_df, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(filtered_df, x=x_axis, y=y_axis)

    st.plotly_chart(fig, use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Télécharger les données filtrées",
        data=csv,
        file_name="parcoursup_filtre.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()

