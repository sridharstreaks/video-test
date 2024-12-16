import streamlit as st
import os
import random
import time

def sample_while():
    i=0
    while i<10:
        print("hi")
        time.sleep(random.randint(0,10))
        i+=1
    return i

with st.spinner("Running function..."):
        result = sample_while()
        os.write(1, f"download_link_fetcher_result: {result}\n".encode())
