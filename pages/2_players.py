import streamlit as st

# configuração da página
st.set_page_config(
    page_title="Players",
    page_icon="⚽️",
    layout="wide"
)

# df da home
df_data = st.session_state['data']

# Selectbox Clubes
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

# Selectbox Jogadores
df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)

# Estatisticas do jogador
player_stats = df_data[df_data['Name'] == player].iloc[0]

# Imagem do jogador / Nome do jogador
st.image(player_stats['Photo'])
st.title(f"{player_stats['Name']}")

# Clube do jogador / Posição / 
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

# Colunas Idade / Altura / Peso
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")

# Barra de divisão / Overall / Barra de progresso
#st.divider()
st.write("---")
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# Colunas Valor de Mercado / Remuneração Semanal / Cláusula de rescisão
col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")

