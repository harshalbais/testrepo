import streamlit as st
import requests
import pandas as pd

ESP_URL = "http://192.168.4.1/attendance.json"

st.title("📋 Attendance Dashboard (From ESP8266)")

try:
    response = requests.get(ESP_URL, timeout=5)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        st.success("Attendance data fetched successfully!")
        st.dataframe(df)

        # Optional: download as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Attendance as CSV",
            data=csv,
            file_name='attendance.csv',
            mime='text/csv',
        )
    else:
        st.error("Failed to fetch attendance data.")
except Exception as e:
    st.warning(f"Could not connect to ESP8266: {e}")
