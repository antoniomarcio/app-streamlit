from json import loads
import streamlit as st
from pandas import read_csv

st.markdown('''
# Visualizador de arquivos
## Suba um arquivo e veja o que acontece 😊❤️
''')

st.text_input(label='Insira o e-mail', max_chars=10)
st.text_input(label='Insira a senha', max_chars=10, type='password')

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
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'text', 'csv':
            df = read_csv(arquivo).transpose()
            st.dataframe(df)
            st.bar_chart(df)
        case 'audio', _:
            st.audio(arquivo)
else:
    st.error('Arquivo não carregado', icon="🚨")