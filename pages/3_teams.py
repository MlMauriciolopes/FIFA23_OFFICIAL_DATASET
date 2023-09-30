import pandas as pd
import streamlit as st

# configuração da página
st.set_page_config(
    page_title="Teams",
    page_icon="🏟️",
    layout="wide"
)

df_data = st.session_state['data']

# Selectbox Clubes
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Selecione AQUI o Clube desejado:", clubes)

df_filtered = df_data[df_data['Club'] == club].set_index("Name")

# Logo e nome do clube
st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                    "Overall" : st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                    "Value(£)": st.column_config.NumberColumn(),
                    "Wage(£)" : st.column_config.ProgressColumn("Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
                    "Photo"   : st.column_config.ImageColumn(),
                    "Flag"    : st.column_config.ImageColumn("Country")
                }, height=800)
