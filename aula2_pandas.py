import pandas as pd
df = pd.read_csv("C:\\Users\\202408652135\\Documents\\analisededados\\imoveis_brasil.csv")
df.shape
df.columns
df.head()
df.tail(5)
df.sample(5)
df.info()

#Verificar os tipos de imóveis
df["Tipo_Imovel"].unique()

#Imoveis com valores maiores que 1M
filtro = df["Valor_Imovel"] > 1000000
df_1M = df.loc[filtro]

#Selecionar cidade, bairro e valor e gravar no df2
colunas_selecionadas = ["Cidade", "Bairro", "Valor_Imovel"]
df2 = df[colunas_selecionadas]

#Ordenar os valores dos imoveis mais caros
df.sort_values("Valor_Imovel")

#Valor medio dos imoveis
valormediogeral = df["Valor_Imovel"].mean()

#Valor medio dos imoveis de Curitiba
filtro = df["Cidade"] == "Curitiba"
df.loc[filtro, ["Valor_Imovel"]].mean()

#Numero de imoveis com valor acima do valor medio
filtro = df["Valor_Imovel"] > valormediogeral
df_maior = df.loc[filtro]
len(df_maior)

#Numero de imoveis com valor abaixo do valor medio
filtro = df["Valor_Imovel"] < valormediogeral
df_menor = df.loc[filtro]
len(df_menor)