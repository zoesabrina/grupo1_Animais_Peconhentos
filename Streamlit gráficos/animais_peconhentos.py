import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

df = pd.read_csv("DADOSSUS_ANIMAIS_PECONHENTOS2017.csv")

st.title('Analise de dados grupo animais peçonhentos')
st.subheader('Pedro, Sabrina, Rianderson, Beatriz, Maria Julia')

sexo_counts = df['Sexo'].value_counts()

st.subheader('Gráfico de distribuição por sexo:')

sexo_counts.plot(kind='bar', figsize=(8, 6), color=['pink', 'coral'])

plt.title('Distribuição por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Contagem')

plt.tight_layout()

st.pyplot(plt)

st.subheader('Quantidade de registros e media das idades por UF:')

media_idade = df.groupby('UF de notificação')["Idade"].mean().reset_index(name='Media de Idades')
quantidade_registros = df.groupby('UF de notificação').size().reset_index(name='Quantidade de Registros')
registro_media = quantidade_registros
registro_media["Media das Idades"]  = media_idade["Media de Idades"]
st.dataframe(registro_media)

st.subheader('Gráfico das quantidades de registros por UF:')

quantidade_registros.plot(x="UF de notificação", y="Quantidade de Registros", kind="bar")

st.pyplot(plt)

st.subheader('Gráfico das medias de idade por UF:')

media_idade.plot(x="UF de notificação", y="Media de Idades", kind="bar")

st.pyplot(plt)

columns_to_plot = ['Tipo de acidente', 'Tipo de acidente - outros',
                   'Serpente - tipo de acidente', 'Aranha - tipo de acidente', 'Lagarta - tipo de acidente']

filtered_df = df[columns_to_plot]
filtered_df = filtered_df.dropna(subset=['Tipo de acidente'])

count_table = filtered_df['Tipo de acidente'].value_counts()

st.subheader('Gráfico de contagem de casos por tipo de acidente:')
fig, ax = plt.subplots(figsize=(7, 3))
count_table.plot(kind='bar', ax=ax, color='green')
plt.xlabel('Tipo de Acidente')
plt.ylabel('Contagem')
plt.title('Contagem de Casos por Tipo de Acidente')
plt.tight_layout()
st.pyplot(plt)

st.subheader('Quantidades de acidentes por município:')
quantidade_municipios = df.groupby(["Município de ocorrência do acidente"])[
    "Município de ocorrência do acidente"].count().reset_index(name="Ocorrências").query(
    "Ocorrências > 510").sort_values(by="Ocorrências", ascending=False)
quantidade_municipios_figure = quantidade_municipios.plot(x="Município de ocorrência do acidente", y="Ocorrências",
                                                          kind="bar", ).get_figure()

st.pyplot(plt)


st.subheader('Quantidades de acidentes por ocupação:')
quantidade_profissao = df.groupby(["Ocupação"])["Ocupação"].count().reset_index(name="Total").sort_values(by='Total',
                                                                                                          ascending=False)
quantidade_profissao_figure = quantidade_profissao.query('Total > 200').plot(x="Ocupação", y="Total",
                                                                             kind="bar").get_figure()
st.pyplot(plt)

st.subheader('Idade por Raça:')

dados = {
    'Idade': [4, 36, 25, 62, 3],
    'Raça': ['Preta', 'Ignorado', 'Indígena', 'Branca', 'Ignorado']
}


plt.bar(dados['Raça'], dados['Idade'])
plt.xlabel('Raça')
plt.ylabel('Idade')
plt.title('Idade por Raça')

st.pyplot(plt)