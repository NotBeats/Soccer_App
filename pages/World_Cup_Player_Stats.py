import streamlit as st
import pandas as pd
import base64

st.title('World Cup Player Stats')

st.markdown("""
Simple webscraping of World Cup stats data.
* **Data Source:** [fbref.com](https://fbref.com/en/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1930, 2023, 4))))

# webscraping of FIFA player stats 
@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/shooting/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(year_selected)

# team selection
sorted_teams = sorted(playerstats.Tm.unique())
team_selected = st.sidebar.multiselect('Squad', sorted_teams, sorted_teams)

# position selection
positions = ['FW', 'MF', 'DF', 'GK']
position_selected = st.sidebar.multiselect('Position', positions, positions)

# filtering data
df_team_selected = playerstats[(playerstats.Tm.isin(team_selected)) & (playerstats.Pos.isin(position_selected))]

st.header('Player Stats in the World Cup')
st.write('Data Dimension: ' + str(df_team_selected.shape[0]) + ' rows and ' + str(df_team_selected.shape[1]) + ' columns')
st.dataframe(df_team_selected)

# download the data as a csv file
def file_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(file_download(df_team_selected), unsafe_allow_html=True)