import streamlit as st
from weather_api import get_weather_data

def run_app():
    st.set_page_config(page_title="Wetter App", page_icon="🌤", layout="centered")
    st.title("🌤 Wetterinformations-App")
    st.markdown("Entwicklung einer App zur Anzeige von aktuellen Wetterdaten (Wintersemester 2022 – 2023)")

    city = st.text_input("Stadtname eingeben:", "Berlin")

    if st.button("Wetter abrufen"):
        result = get_weather_data(city)
        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"Wetter in {result['city']}:")
            st.metric("🌡 Temperatur", f"{result['temp']} °C")
            st.metric("💧 Luftfeuchtigkeit", f"{result['humidity']} %")
            st.metric("🌬 Wind", f"{result['wind']} m/s")
            st.metric("🔵 Druck", f"{result['pressure']} hPa")
            st.markdown(f"**Beschreibung:** {result['description'].capitalize()}")
            icon_url = f"http://openweathermap.org/img/wn/{result['icon']}@2x.png"
            st.image(icon_url)
