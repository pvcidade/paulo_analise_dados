import pandas as pd
arquivo = "C:\\Users\\202408652135\\Documents\\analisededados\\titanic.csv"
df = pd.read_csv(arquivo)

df.shape
df.columns
df.info()
df.isna().sum()

filtro = df["Fare"].isna()
df.loc[filtro]

filtro2 = df["Age"].isna()
df.loc[filtro2]
media_idade = df["Age"].mean()
df["Age"].fillna(0)
df["Age"] = df["Age"].fillna(media_idade)

filtro3 = df["Sex"]=="male"
df_homem = df.loc[filtro3]
df_homem["Age"].mean()

filtro4 = df["Sex"]=="female"
df_mulher = df.loc[filtro4]
df_mulher["Age"].mean()

df.groupby("Sex")["Age"].mean()

filtro5 = (df["Sex"]=="female") & (df["Survived"]==1)
df_msobrevivente = df.loc[filtro5]

df["FamilyMembers"] = df["SibSp"] + df["Parch"] + 1
