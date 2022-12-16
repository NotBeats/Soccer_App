import streamlit as st
import pandas as pd
import base64

st.title('World Cup Group Stage')

st.markdown("""
Simple webscraping of World Cup stats data.
* **Data Source:** [fbref.com](https://fbref.com/en/)
""")

st.sidebar.header('User Input Features')
year_selected = st.sidebar.selectbox('Year', list(reversed(range(1930, 2023, 4))))

# webscraping of FIFA player stats 
@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group A')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[1]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group B')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[2]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group C')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[3]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group D')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[4]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group E')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[5]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group F')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[6]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group G')
st.dataframe(teamstats)

@st.cache
def load_data(year):
    url = "https://fbref.com/en/comps/1/" + str(year) + "/" + str(year) + "-World-Cup-Stats"
    html = pd.read_html(url, header=0)
    df = html[7]
    raw = df.drop(df[df.Squad == 'Squad'].index) # deletes repeating headers in content
    raw = raw.fillna(0)
    teamstats = raw.drop(['Rk'], axis=1)
    return teamstats
teamstats = load_data(year_selected)

st.header('Group H')
st.dataframe(teamstats)