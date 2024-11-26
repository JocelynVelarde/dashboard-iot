#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import requests

#######################
# Page configuration
st.set_page_config(
    page_title="Secure Sense 🔐",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)


#######################
# Load data


#######################
# Sidebar
with st.sidebar:
    st.title('🏡 Secure Sense Dashboard')
    
    


#######################


# Donut chart
def make_donut(input_response, input_text, input_color):
  if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
  if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
  if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
  if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
  source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
  })
  source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
  })
    
  plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
  ).properties(width=130, height=130)
    
  text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
  plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
  ).properties(width=130, height=130)
  return plot_bg + plot + text

# Convert population to text 
def format_number(num):
    if num > 1000000:
        if not num % 1000000:
            return f'{num // 1000000} M'
        return f'{round(num / 1000000, 1)} M'
    return f'{num // 1000} K'

# Calculation year-over-year population migrations
def calculate_population_difference(input_df, input_year):
  selected_year_data = input_df[input_df['year'] == input_year].reset_index()
  previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
  selected_year_data['population_difference'] = selected_year_data.population.sub(previous_year_data.population, fill_value=0)
  return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.population, selected_year_data.population_difference], axis=1).sort_values(by="population_difference", ascending=False)


#######################
# Dashboard Main Panel
col = st.columns((1.5, 3, 1.5), gap='medium')

with col[0]:
    df_population_difference_sorted = calculate_population_difference(df_reshaped, selected_year)

    response_sensor_count = requests.get("https://fast-api-reto.onrender.com/count-sensors")
    response_recent_sensor = requests.get("https://fast-api-reto.onrender.com/recent-sensor")
    if response_sensor_count.status_code == 200:
        sensor_data_count = int(response_sensor_count.json()[0][f"COUNT(*)"])
        recent_data_sensor = response_recent_sensor.json()[0].get("type_")
        st.metric(label="Sensor Count", value=sensor_data_count, delta=recent_data_sensor)
    else:
        st.error(f"Failed to fetch data: {response_sensor_count.status_code}")

    response_person_count = requests.get("https://fast-api-reto.onrender.com/count-persons")
    response_recent_person = requests.get("https://fast-api-reto.onrender.com/recent-person")
    if response_person_count.status_code == 200:
        person_data_count = int(response_person_count.json()[0][f"COUNT(*)"])
        recent_data_person = response_recent_person.json()[0].get("name")
        st.metric(label="Person Count", value=person_data_count, delta=recent_data_person)
    else:
        st.error(f"Failed to fetch data: {response_person_count.status_code}")

    response_house_count = requests.get("https://fast-api-reto.onrender.com/count-houses")
    response_resent_house = requests.get("https://fast-api-reto.onrender.com/recent-house")
    if response_house_count.status_code == 200:
        house_data_count = int(response_house_count.json()[0][f"COUNT(*)"])
        recent_data_house = response_resent_house.json()[0].get("direction")
        st.metric(label="House Count", value=house_data_count, delta=recent_data_house)
    else:
        st.error(f"Failed to fetch data: {response_house_count.status_code}")

    response_room_count = requests.get("https://fast-api-reto.onrender.com/count-rooms")
    response_recent_room = requests.get("https://fast-api-reto.onrender.com/recent-room")
    if response_room_count.status_code == 200:
        room_data_count = int(response_room_count.json()[0][f"COUNT(*)"])
        recent_data_room = response_recent_room.json()[0].get("num_windows")
        st.metric(label="Room Count", value=room_data_count, delta=recent_data_room)
    else:
        st.error(f"Failed to fetch data: {response_room_count.status_code}")
    

with col[1]:
    donut_chart_ultrasonic = make_donut(1, 'Inbound Migration', 'green')
    donut_chart_sound = make_donut(99, 'Outbound Migration', 'red')
    donut_chart_push = make_donut(49, 'Outbound Migration', 'green')
    donut_chart_ir = make_donut(12, 'Outbound Migration', 'green')
    donut_chart_magnetic = make_donut(78, 'Outbound Migration', 'red')
    migrations_col = st.columns((1, 2, 2))
    with migrations_col[1]:
        st.write('Ultrasonic Active')
        st.altair_chart(donut_chart_ultrasonic)
        st.write('Sound Active')
        st.altair_chart(donut_chart_sound)
    with migrations_col[2]:
        st.write('Push Button Active')
        st.altair_chart(donut_chart_push)
        st.write('IR Active')
        st.altair_chart(donut_chart_ir)
        st.write('Magnetic Active')
        st.altair_chart(donut_chart_magnetic)
    
with col[2]:
    
    with st.expander('About our dashboard', expanded=True):
        st.write('''
            - :orange[**Counts**]: display the amount of elements in a specific section, it also displays the most recent element added in green
            - :orange[**Active alerts**]: display the percentage of total time an alarm was active
            ''')