# BI Project

Cette application Streamlit propose une interface pour explorer les données
publiques de Parcoursup. Les données sont chargées depuis Data.gouv.fr et des
filtres dynamiques permettent de naviguer dans le jeu de données.

## Fonctionnalités

- **Chargement automatique des données** via un cache pour accélérer les
  exécutions suivantes.
- **Filtres interactifs** générés automatiquement à partir des colonnes du jeu
  de données (catégorielles et numériques).
- **Statistiques descriptives** pour obtenir une vision rapide du contenu.
- **Graphiques interactifs** grâce à Plotly.

## Démarrage rapide

```bash
pip install -r requirements.txt
streamlit run parcoursup.py
```

L'application est également disponible à l'adresse suivante :
https://samirelhassani1998-bi-project-parcoursup-j363e2.streamlit.app/
