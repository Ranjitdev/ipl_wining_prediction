import streamlit as st

with st.form('submit form'):
    st.write('form')

    submit = st.form_submit_button('Submit')
    if submit:
        st.write('Submitted')