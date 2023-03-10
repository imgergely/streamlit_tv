import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
import streamlit.components.v1 as components

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')


@st.experimental_singleton
def getlink(url):
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    time.sleep(0.5)
    driver.get(url)
    time.sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html')


    return soup.find('source')['src']

def run(url,mediatype):
    components.html(
    """
        <div style="display: flex; justify-content: center; align-items: center;">
        <video controls autoplay="true" id="video">
            <source src= {0} type="{1}"/>
        </video>
        </div>

        <script>

        const video = document.getElementById('video');
        let previousTime = video.currentTime;

        setInterval(() => {{
        if (video.currentTime < 1000) {{
            video.load();
        }}
        }}, 2000);

        </script>

    """.format(url,mediatype), width=1070, height=768)


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
        run(link,"video/mp4")
    if rtl:
        link = getlink("https://onlinestream.live/rtl/videoplayer/6141-2")
        run(link,"video/mp4")

    if ujra:
        st.experimental_rerun()

if __name__ == "__main__":
    app()
