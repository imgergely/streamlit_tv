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
        
        <script>

        const video = document.getElementById('video');
        let previousTime = video.currentTime;

        setInterval(() => {{
        if (video.currentTime < 1000) {{
            console.log('Video is NOT playing');
            video.load();
        }}
        }}, 2000);

        </script>

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
