# Revisao dicionario
dic = {
    "nome":"Laerte",
    "idade": 46,
    "email":"laerte@laerte.com"
}
# Para acessar a chave nome
dic["nome"]
# Para acessar a chave idade
dic["idade"]
# Para acessar a chave email
dic["email"]
# Transfomar par DataFrame
import pandas as pd
df = pd.DataFrame([dic])
# API VIACEP.com.br

cep = "70686540"
url = f"https://viacep.com.br/ws/{cep}/json/"
response = requests.get(url)
dic_cep = response.json()
# Api do ipeadata.gov.br
import requests
url = "http://www.ipeadata.gov.br/api/odata4/Metadados"
response = requests.get(url)
metadados = response.json()
metadados = metadados["value"]
df = pd.DataFrame(metadados)




# Acessar o cogigo do IBGE
SERCODIGO = "HOMIC"
url = f"http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{SERCODIGO}')"
response = requests.get(url)
dados = response.json()
dados = dados["value"]
df = pd.DataFrame(dados)
df.shape
df.columns
df.info()
df["VALDATA"] = pd.to_datetime(df["VALDATA"], errors="coerce")
df["VALDATA"] = df["VALDATA"].dt.year
df["VALDATA"].unique()
filtro = df["NIVNOME"]=="Brasil"
df_brasil = df.loc[filtro]
df_brasil[["VALDATA", "VALVALOR"]].plot()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Plot
ax = df_brasil[["VALDATA", "VALVALOR"]].plot(x="VALDATA", y="VALVALOR", legend=False)
# Formatação do eixo X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))  # ou '%Y-%m-%d' conforme sua preferência
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import requests
api = "http://api.football-data.org/v4/areas/"
response = requests.get(api)
response.json()


import requests
import pandas as pd
uri = 'https://api.football-data.org/v4/matches'
headers = { 'X-Auth-Token': '6edd9884f02c4a2facb386317f3d8440' }

response = requests.get(uri, headers=headers)
matches = response.json()["matches"]
pd.DataFrame(matches)
