import requests
from lxml import html
import time
import random
import streamlit as st
import os

payload = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
'Accept-Language': 'da, en-gb, en',
'Accept-Encoding': 'gzip, deflate, br',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Referer': 'https://www.google.com/'
}

def get_domian(search_keyword,as_sitesearch=None):
    dicto={}
    if as_sitesearch is None:
        url=f'https://www.google.com/search?q={search_keyword.replace(" ", "+")}'
        response = requests.get(url, headers= payload)
        if response.status_code==200:
            tree = html.fromstring(response.content)
            domain_name=str(tree.xpath('//div[@class="yuRUbf"]//a[@href and not(@disabled)]/@href')[0]).replace("https://", "").replace("/", "")
        return domain_name
    else:
        url=f'https://www.google.com/search?q={search_keyword.replace(" ", "+").lower()}&as_sitesearch={as_sitesearch}'
        response = requests.get(url, headers= payload)
        if response.status_code==200:
            tree = html.fromstring(response.content)
            movie_url=str(tree.xpath(f'//div[@class="yuRUbf"]//a[contains(@href,"movie/page") or contains(@href,{search_keyword.replace(" ", "-").lower()}) and not(contains(@href,"google"))]/@href')[0])
            dicto[search_keyword]=movie_url
        return dicto
        
def download_link_fetcher(dicto):
    while not any(".dl" in value or ".mp4" in value for value in dicto.values()):
        os.write(1, ".mp4 not found. Continuing the loop.\n".encode())
        if len(dicto) > 0:
            *_, last = dicto.values()
        print(last)
        response = requests.get(last, headers= payload)
        tree = html.fromstring(response.content)
        if tree.xpath('count(//div[@class="f"])') > 0 and tree.xpath('count(//div[@class="bf"]//div[@class="f"])') == 0:
            try:
                dicto[tree.xpath('//div[@class="f"]//a//font[not(contains(text(),"Sample"))]/text()')[0]] = "https://3moviesda.com"+tree.xpath('//div[@class="f"]//a//font[not(contains(text(),"Sample"))]//parent::a/@href')[0]
            except IndexError:
                dicto[tree.xpath('//div[@class="f"]//a[not(contains(text(),"Sample"))]/text()')[0]] = "https://3moviesda.com"+tree.xpath('//div[@class="f"]//a[not(contains(text(),"Sample"))]//parent::a/@href')[0]
        elif tree.xpath('count(//div[@class="dlink"]//a[not(contains(@rel,"norefferrer"))])') > 0:
            dicto[tree.xpath('//div[@class="dlink"]//a/text()')[0]] = tree.xpath('//div[@class="dlink"]//a/text()//parent::a/@href')[0]
        elif tree.xpath('count(//div[@class="dlink"]//a[contains(@rel,"norefferrer")])') > 0:
            dicto[tree.xpath('//div[@class="dlink"]//a/text()')[0]] = tree.xpath('//div[@class="dlink"]//a/text()//parent::a/@href')[0]
            #dicto[tree.xpath('//a/text()')]=tree.xpath('//a/text()//parent::a/@href')
        else:
            print("error")
            break
        time.sleep(random.randint(0,10))
    return dicto

def get_streamlink(dicto):
    *_, last = dicto.values()
    return last

st.set_page_config(
    page_title="Streaks Movies - Your New Movie Experience",
    page_icon=":sparkles:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Streamlit app
st.title("Text to Video Player")

if st.button("Submit"):
    # Trigger first function
    get_domian_result = get_domian(input_text,"3moviesda.com")
    os.write(1, f"{get_domian_result}\n".encode())

    with st.spinner("Running function..."):
        download_link_fetcher_result = download_link_fetcher(get_domian_result)
        os.write(1, f"download_link_fetcher_result: {download_link_fetcher_result}\n".encode())
         # Trigger second function with the result of the first

    # Final streaming link extractor
    try:
        video_path = get_streamlink(download_link_fetcher_result)
        os.write(1, f"video_path: {video_path}\n".encode())
    except Exception as e:
        st.error(f"Error in get_streamlink: {str(e)}")
        st.stop()


# Display the video if the file exists
try:
    st.video(video_path,format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)
except Exception as e:
    st.error(f"An error occurred: {str(e)}")



