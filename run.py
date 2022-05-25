from libraries import *
import streamlit as st


st.set_page_config(page_title='Covid Dashboard', page_icon="💉")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
   .sidebar .sidebar-content {
        background: url("http://wp.bssnews.net/wp-content/uploads/2020/05/GettyImages-1209679043.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

countries = ['Sri Lanka', 'United States',
             'United Kingdom', 'Italy', 'India', 'China']
country_code = {'Sri Lanka': 'lk', 'United States': 'us',
                'United Kingdom': 'gb', 'China': 'cn', 'India': 'in', 'Italy': 'it'}
data_types = ['cases', 'deaths', ]


country = st.sidebar.selectbox('Select Country', countries)

days = st.sidebar.slider('Select Days', min_value=1, max_value=90)
data_type =data_types

total_cases = get_historic_cases(country, str(days))
total_deaths = get_historic_deaths(country, str(days))
total_recoveries = get_historic_recoveries(country, str(days))
total_df = pd.concat(
    [total_cases, total_deaths, total_recoveries], axis=1).astype(int)

daily_cases = get_daily_cases(country, str(days))
daily_deaths = get_daily_deaths(country, str(days))
daily_recoveries = get_daily_recoveries(country, str(days))
daily_df = pd.concat(
    [daily_cases, daily_deaths], axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country,)
yesterday_deaths = get_yesterday_deaths(country,)
yesterday_recoveries = get_yesterday_recoveries(country,)
st.title('🧫Covid Dashboard💉')

col1, col2 = st.columns(2)
column1, column2, column3 = st.columns(3)
col1.metric(label='Country', value=country)
col2.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")
column1.metric('Total Cases', yesterday_cases)
column2.metric('Total Deaths', yesterday_deaths)
column3.metric('Total recovered', yesterday_recoveries)




with st.sidebar.expander("About"):
         st.write( "Developed by red pndemic beaters of Meu Labs ")

with st.sidebar.expander("Version"):
    st.write("2.1.5")

st.line_chart(daily_cases)
st.line_chart(daily_deaths)
st.info('You must pick the number of Days for the comparison')

st.line_chart(daily_df[data_type])
st.video('https://www.youtube.com/watch?v=5DGwOJXSxqg')

st.balloons()

st.subheader("Thank You for using our Covid Dashboard")



st.info('Below buttons are to download these codes')
lib_code_contents = '''
import requests
import pandas as pd
def get_historic_cases(country, days):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  cases_df = pd.DataFrame(data=data['timeline']['cases'].values(), 
                    index=data['timeline']['cases'].keys(),
                    columns=['cases'])
  return cases_df
def get_historic_deaths(country, days):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  deaths_df = pd.DataFrame(data=data['timeline']['deaths'].values(), 
                    index=data['timeline']['deaths'].keys(),
                    columns=['deaths'])
  return deaths_df
def get_historic_recoveries(country, days):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
  data = resp.json()
  recoveries_df = pd.DataFrame(data=data['timeline']['recovered'].values(), 
                    index=data['timeline']['recovered'].keys(),
                    columns=['recovered'])
  return recoveries_df
def get_yesterday_cases(country):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['cases'].values())[0]
  return count 
def get_yesterday_deaths(country):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['deaths'].values())[0]
  return count 
def get_yesterday_recoveries(country):
  resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays=1')
  data = resp.json()
  count = list(data['timeline']['recovered'].values())[0]
  return count 
def get_daily_cases(country,days):
    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['cases'].values(), 
                    index=data['timeline']['cases'].keys(),
                    columns=['cases'])
    daily = cumilative.diff().fillna(0)
    return daily 
    
def get_daily_deaths(country,days):
    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['deaths'].values(), 
                    index=data['timeline']['deaths'].keys(),
                    columns=['deaths'])
    daily = cumilative.diff().fillna(0)
    return daily 
def get_daily_recoveries(country,days):
    resp = requests.get(f'https://disease.sh/v2/historical/{country}?lastdays={days}')
    data = resp.json()
    cumilative = pd.DataFrame(data=data['timeline']['recovered'].values(), 
                    index=data['timeline']['recovered'].keys(),
                    columns=['recovered'])
    daily = cumilative.diff().fillna(0)
    return daily 
'''
st.download_button('Tap to download the library code', lib_code_contents)

application_code_contents = '''
import pandas as pd
import streamlit as st
from libraries import *
st.set_page_config(page_title='Covid Dashboard', page_icon="💉")
countries = ['Australia', 'China','India','Italy', 'Japan', 'USA', 'UK', 'Sri Lanka', 'Spain', 'Brazil']
data_types = ['cases', 'deaths', 'recovered']
country = st.sidebar.selectbox('Pick a country', countries)
days = st.sidebar.slider('Pick your days', min_value=1,max_value=90)
data_type = st.sidebar.multiselect('Pick data types', data_types)
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
st.sidebar.write("  ")
with st.sidebar.expander("About"):
         st.write( "Developed by Casual Coders")
with st.sidebar.expander("Version"):
    st.write("1.0.1")
cases_df = get_historic_cases(country,days)
deaths_df = get_historic_deaths(country,days)
recoveries_df = get_historic_recoveries(country,days)
historic_df = pd.concat([cases_df,deaths_df,recoveries_df],axis=1).astype(int)
daily_cases_df = get_daily_cases(country,days)
daily_deaths_df = get_daily_deaths(country,days)
daily_recoveries_df = get_daily_recoveries(country,days)
daily_df = pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)
yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)
st.title('Covid Dashboard')
st.metric('Country', country)
st.metric('Total Cases', yesterday_cases)
st.metric('Total Deaths', yesterday_deaths)
st.metric('Total recovered', yesterday_recoveries)
st.area_chart(daily_df[data_type])
'''
st.download_button('Tap to download the application code', application_code_contents)