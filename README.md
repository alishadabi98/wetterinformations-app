# 🌤 Wetterinformations-App

**Technologien:** Python, Requests, Streamlit, OpenWeatherMap API

## 🔍 Beschreibung
Diese App ruft aktuelle Wetterdaten über die OpenWeatherMap API ab und zeigt diese übersichtlich an. Der Benutzer kann eine Stadt eingeben, und erhält:

- Temperatur
- Luftfeuchtigkeit
- Luftdruck
- Windgeschwindigkeit
- Wetterbeschreibung + Icon



## 🚀 Starten
```bash
pip install -r requirements.txt
streamlit run ui_streamlit.py
```

## ⚙️ Features
- Fehlerbehandlung für ungültige Stadtnamen
- Caching und History-Datei
- Moderne UI (Streamlit)
- Modular aufgebaut
