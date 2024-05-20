## ctrl+c interromper o streamlit
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Hash&Co ao longo de maio")
    st.write("Quer aprender Python? [Clique aqui](https://www.hashtagtreinamentos.com/?origemurl=75502579145&gad_source=1&gclid=CjwKCAjwupGyBhBBEiwA0UcqaJ-UUZ-UZX1TWbWctgyaFOuRaf1DR0jsVlwPIwfEJ2wyXTLSUOaVchoCwTwQAvD_BwE)")

with st.container():
    st.write("---")
    dados = pd.read_csv("resultados.csv")
    st.area_chart(dados, x="Data", y="Contratos")