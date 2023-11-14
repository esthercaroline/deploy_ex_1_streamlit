import streamlit as st
import requests

st.title('Informações do País')

#Criação do input de texto e botão de busca

pais = st.text_input("Digite o nome de um país em inglês:")
infos = st.button("Buscar")

if infos:

    #Conexão com a API
    r = requests.get(f'https://restcountries.com/v3.1/name/{pais}?fullText=true')
    if 'status' in r.json():
        st.write('País não encontrado, verifique se escreveu corretamente e em inglês')
    else:
        expander = st.expander('Resultados')
#Criação do expander resultados com dois containers
        with expander:
            container1 = st.container()
            container_bandeira = st.container()

            #Criação do container 1 com duas colunas do mesmo tamanho
            with container1:
                col1,col2 = st.columns([2,2])
                with col1:
                    st.write('***Nome oficial:***')
                    st.write(r.json()[0]['name']['official'])

                    st.write('***Países que fazem fronteira:***')
                    fronteiras = r.json()[0]['borders']
                    for pais in fronteiras:
                        st.write(f'Fronteira com {pais}')

                    st.write('***Latitude***')
                    st.write(r.json()[0]['latlng'][0])
                    st.write('***Longitude***')
                    st.write(r.json()[0]['latlng'][1])
                
                with col2:
                    arma = r.json()[0]['coatOfArms']
                    if arma is None:
                        st.write('Esse país não possui brasão de armas')
                    else:
                        st.image(arma['png'])
        #Criação do container com a imagem da bandeira
            with container_bandeira:
                bandeira = r.json()[0]['flags']
                st.image(bandeira['png'], use_column_width= True)


                        




