import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']
    
    with st.form(key='insert'):
        input_nome_empresa = st.text_input(label='Insira o nome da empresa:')
        input_endereço = st.text_input(label='Insira o endereço:')
        input_telefone = st.number_input(label='Insira o telefone:', format='%d', step=1)
       
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.inserir(input_nome_empresa, input_endereço, input_telefone)
            st.success('empresa incluido com sucesso')