import streamlit as st
import os
import random
import time
import requests
from lxml import html

d={}

def get_domain(i):
    response=requests.get("https://randomuser.me/api/")
    tree = html.fromstring(response.content)
    d[i]=tree.xpath('//text()')
    time.sleep(random.randint(0,3))
    return d

def count_characters_in_dict_values(my_dict):
    total_count = 0
    for value in my_dict.values():
        if isinstance(value, str):  # Check if the value is a string
            total_count += len(value)
        time.sleep(10)
    return total_count

def display_result(result):
    return result/2
    

result = get_domain(2)

with st.spinner("Running function..."):
        result_2 = count_characters_in_dict_values(result)

result_3 = display_result(result_2)
os.write(1, f"download_link_fetcher_result: {result_3}\n".encode())
