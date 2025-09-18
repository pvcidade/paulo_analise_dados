import pandas as pd
file = "C:\\Users\\202408652135\\Documents\\analisededados\\cadastro_alunos.xlsx"
df = pd.read_excel(file)
filtro = df["nome_aluno"].str.contains("^sabrina|ana|lucas", regex = True, case= False)
df.loc[filtro]

import requests
import json
import pandas as pd

url = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': 'e927d635b04345f0b4bc12327715de0a' }
response = requests.get(url, headers=headers)
response = response.json()
matches = response["matches"]
df = pd.DataFrame(matches)

