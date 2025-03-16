import pandas as pd
import requests
import json
from datetime import datetime
from io import StringIO

GEO_CODE = '3509502'

current_week = datetime.now().isocalendar()[1] 
current_year = datetime.now().year

url = f"https://info.dengue.mat.br/api/alertcity?geocode={GEO_CODE}&disease=dengue&format=csv&ew_start={current_week -1}&ew_end={current_week}&ey_start={current_year}&ey_end={current_year}"

response = requests.get(url)
data = response.content.decode("utf-8")

df_data = pd.read_csv(StringIO(data))

df_data.to_excel(f'data/Cases_Dengue_week_{current_week}.xlsx', index = False)