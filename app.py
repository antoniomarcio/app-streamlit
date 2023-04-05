from json import loads
import streamlit as st
from pandas import read_csv

st.markdown('''
# Visualizador de arquivos - Antônio Márcio
## Suba um arquivo e veja o que acontece 😊❤️
''')

arquivo = st.file_uploader(
    label='Suba seu arquivo aqui',
    type=['jpg', 'png', 'py', 'mp3', 'csv', 'json']
)

if arquivo:
    print(arquivo.type)
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'application', 'octet-stream':
            st.code(arquivo.read().decode())
        case 'text', 'csv':
            df = read_csv(arquivo).transpose()
            st.dataframe(df)
            st.bar_chart(df)
        case 'audio', _:
            st.audio(arquivo)
else:
    st.error('Arquivo não carregado', icon="🚨")
