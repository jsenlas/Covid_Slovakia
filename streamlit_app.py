import streamlit
import urllib.request

files = [
    "OpenData_Slovakia_Covid_DailyStats_Regions.csv",
    "OpenData_Slovakia_Covid_DailyStats.csv",
    "OpenData_Slovakia_Covid_DailyStats_Regions_ALL.csv"
]


filename, headers = urllib.request.urlretrieve("https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv", filename="OpenData_Slovakia_Covid_DailyStats.csv")
print(filename)

