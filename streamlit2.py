import streamlit as st
headerSection = st.container
mainSection = st.container
LeftNav = st.sidebar
with headerSection:
  st.title("Stremlit")
  st.markdown("Blabla")
with LeftNav:
  st.title("LV")
  st.markdown("DD")
