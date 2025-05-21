import streamlit as st
name = st.text_input("Enter Your Name : ")
frame = st.text_input("Enter your Father Name : ")
adr = st.text_area("Enter Your Text : ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5,6,7,8,9,10,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {frame}
    address : {adr}
    class : {classdata}""")
    

