import streamlit as st
import urllib.request
import pandas as pd
import numpy as np

st.title('Hnusoba v obrazkoch')

files = [
    "OpenData_Slovakia_Covid_DailyStats_Regions.csv",
    "OpenData_Slovakia_Covid_DailyStats.csv",
    "OpenData_Slovakia_Covid_DailyStats_Regions_ALL.csv"
]




@st.cache
def get_data():
    print("Getting data")
    filename, headers = urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv",
        filename="OpenData_Slovakia_Covid_DailyStats.csv")

    # return pd.read_csv("https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv", header=None, delimiter=";")
    fp = open(filename, "r")
    return [i.split(";") for i in fp.readlines()][1:100]
try:
    data = [int(i[2]) for i in get_data()]

    type(data)



    print(data)
    st.line_chart(data=data, width=20, height=200, use_container_width=True)

except Exception as e:
    print(e)