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

# Sidebar
st.sidebar.markdown('Desenvolvido por [Asimov Academy]')
st.sidebar.markdown('Melhorado por [Maurício Lopes]')
st.sidebar.link_button("Download do Dataset do Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data/")

st.markdown(
    """
    O conjunto de dados de jogadores de futebol de 2017 a 2023 é uma coleção abrangente de informações sobre jogadores de futebol profissionais. Inclui detalhes como dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes de contratos, afiliações de clubes, valores de mercado, salários, posições preferenciais, taxas de trabalho, classificações de habilidades e desenvolvimento de jogadores.
        
    ## COMO UTILIZAR ESSA APLICAÇÃO:
    Se você estiver utilizando um smartfone, no canto **superior esquerdo**, tem uma seta que abre o menu de opções, com as seguintes abas:

    ### Home: 
    Página inicial dessa aplicação.
    ### Players: 
    Mostra o nome do clube, e o jogador correspondente dele.

    ### Teams:
    Seleciona o clube e mostra as informações de todos os jogadores. A ordem inicial é em Ordem **Overall**.

    ### Extra:
    Você também pode além de selecionar da forma padrão de drop down, digitar na aba de seleção de clubes, além de clicar no gráfico e alterar a ordem das informações (crescente e decrescente).
    """
)