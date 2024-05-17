import main as la
import streamlit as st


st.set_page_config(layout="wide")
st.title("Decoder JWT")
token = st.sidebar.text_area(label="Insira o JWT")

if token:
    response = la.decode_jwt(token)
    st.text("Payload:")
    st.text(response)