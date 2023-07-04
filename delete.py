from numpy import delete
import streamlit as st

import controller.cliente as cliente

def deletar():
    st.session_state.dele = False
    st.title('Deletar dados')

    with st.form(key='delete'):
        delete_id = st.number_input (label = 'Insira o id') 
        button_delete_select = st.form_submit_button('deletar')
 
        if button_delete_select:
            cliente.deletar(int(delete_id))
            st.success('Cliente deletado com sucesso!!!')