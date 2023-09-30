# imports
import streamlit as st
import pandas as pd 
import webbrowser
from datetime import datetime

# dataset + filtros
if 'data' not in st.session_state:
    df_data = pd.read_csv('dataset/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data

# Texto
st.write("# FIFA 23 OFFICIAL DATASET ⚽️!")

st.sidebar.markdown('Desenvolvido por [Asimov Academy]')
btn = st.button(" Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/')

st.markdown(
    """
    The Football Player Dataset from 2017 to 2023 is a comprehensive collection of information about professional football players. It includes details such as player demographics, physical characteristics, playing statistics, contract details, club affiliations, market values, wages, preferred positions, work rates, skill ratings, and player development.
    """
)