import streamlit as st
import requests
API_KEY=st.secrets['APIKey']
st.title("WeatherApp")
st.header("My Weather App")

location = st.text_input("Enter the location", value="Hanoi")
st.write("You entered:", location)
if location: 

    # Define the API endpoint URL
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={API_KEY}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the weather data from the response
        geo_data = response.json()
        print(geo_data)
        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]
        st.write(lat, lon)
    else:
        print("Error: Failed to retrieve weather data")
        print(response.json())

    # Define the API endpoint URL
    # response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Hanoi&appid={api_key}&units=metric")
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the weather data from the response
        weather_data = response.json()
        st.metric("Feel like",weather_data["main"]['feels_like'])
        # weather_data
    else:
        print("Error: Failed to retrieve weather data")
        print(response.json())

