import streamlit as st

def sample_while():
    i=0
    while i<10:
        print("hi")
        i+=1
    return i

with st.spinner("Running function..."):
        result = sample_while()
        os.write(1, f"download_link_fetcher_result: {result}\n".encode())
