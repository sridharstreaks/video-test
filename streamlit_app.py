import streamlit as st
import os
import random
import time

d ={'Name':'Steve', 'Age':30, 'Designation':'Programmer', 'Salary':'100k', 'Country':'USA'}

def sample_while():
    i=0
    while i<len(d):
        os.write(1, "hi\n".encode())
        time.sleep(random.randint(0,10))
        i+=1
    return i

with st.spinner("Running function..."):
        result = sample_while()
        os.write(1, f"download_link_fetcher_result: {result}\n".encode())
