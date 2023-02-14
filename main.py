import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
import streamlit.components.v1 as components


def getlink(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(0.5)
    driver.get(url)
    time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'html')

    video = soup.find('video')

    link = ""
    for i in video:
        link+=i['src']
    return link

def run(url):
    components.html(
    """
        <video controls autoplay="true" id="video">
        <source src={} type="video/mp4" />
        </video>

    """.format(url), width=1050, height=768)


def app():

    col1, col2, col3= st.columns([1,2,4])

    with col1:
        tv2 = st.button("TV2")
    with col2:
        rtl = st.button("RTL")
    with col3:
        ujra = st.button("ÚJRATÖLT")

    if tv2:
        link = getlink("https://onlinestream.live/tv2/videoplayer/6143-2")
        run(link)
       
    if rtl:
        link = getlink("https://onlinestream.live/rtl/videoplayer/6141-2")
        run(link)

    if ujra:
        st.experimental_rerun()

if __name__ == "__main__":
    app()
