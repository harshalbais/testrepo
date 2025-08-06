import streamlit as st
import requests
import pandas as pd
import socket

ESP_URL = "http://192.168.4.1/attendance.json"

st.title("📋 Attendance Dashboard (From ESP8266)")
def is_connected_to_esp():
    try:
        socket.create_connection(("192.168.4.1", 80), timeout=2)
        return True
    except OSError:
        return False

if is_connected_to_esp():
    # proceed with fetching attendance
    data = requests.get("http://192.168.4.1/attendance.json", timeout=5).json()
else:
    st.error("Not connected to ESP8266. Please connect to its hotspot.")
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
