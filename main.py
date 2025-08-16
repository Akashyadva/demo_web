import streamlit as st

name= st.text_input("enter your name")
fname= st.text_input("enter your father name")
adr= st.text_area("enter your Text : ")
classdata = st.selectbox("Select your class :",(1,2,3,4,5,6))

button = st.button("done")
if button:
    st.markdown(f"""
    name:{name}
    fathername:{fname}
    adddress:{adr}
    classdata:{classdata}
    """)