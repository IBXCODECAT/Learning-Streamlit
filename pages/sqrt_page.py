import streamlit as st
from utility.sqrt import square_number

st.title("Square Calculator")

num = st.number_input("Enter a number", value=0)
result = square_number(num)

st.write(f"The square of {num} is {result}")
