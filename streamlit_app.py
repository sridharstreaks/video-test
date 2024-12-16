import streamlit as st
import os
import random
import time
import requests
from lxml import html

def sample_while():
    i=0
    last=''
    d ={}
    whi not any("Ukraine" in value or "America" in value for value in d.values()):
        os.write(1, ".mp4 not found. Continuing the loop.\n".encode())
        if len(d) > 0:
            *_, last = d.values()
            os.write(1, f"{last}\n".encode())
        response=requests.get("https://randomuser.me/api/")
        tree = html.fromstring(response.content)
        d[i]=tree.xpath('//pre/text()')
        i+=1
    return d

with st.spinner("Running function..."):
        result = sample_while()
        os.write(1, f"download_link_fetcher_result: {result}\n".encode())
