import numpy as np
import requests
import folium
import streamlit as st

def fetch_data():
    url = "https://a.windbornesystems.com/treasure/00.json"
    response = requests.get(url)
    data = response.json()
    data = np.array(data)
    data = data[~np.isnan(data).any(axis=1)]
    return data

st.title("Live Sounding Balloon Data")

data = fetch_data()

world_map = folium.Map(location=[data[0, 0], data[0, 1]], zoom_start=2)

for point in data:
    lat, lon, alt = point[0], point[1], point[2]

    folium.CircleMarker(
        location=[lat, lon],
        radius=alt,  
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.3,  
        popup=f"Altitude: {alt:.2f}m"
    ).add_to(world_map)

st.subheader("Sounding Balloon Map")

st.markdown(
    "**Note:** The position is derived from the latitude and longitude coordinates, and the radius represents the altitude of the balloon. Zoom in to see it clearly."
)
st.components.v1.html(world_map._repr_html_(), height=600)
st.write("")

