

import streamlit as st
import streamlit.components.v1 as components


def run(url):
    components.html(
    """
    <video controls autoplay="true" id="video">
    <source 
        src={}
        type="video/mp4" />
    </video>
    """.format(url),
    height=1754,
    width=1024)


def app():
    col1, col2= st.columns([0.3 ,1])
    with col1:
        tv2 = st.button("TV2")
    with col2:
        rtl = st.button("RTL")

    if tv2:
        run("https://cdn.mediaklikk.org:443/tv2/0MjMxEjMxITM")
       

    if rtl:
        run("https://cdn.mediaklikk.org:443/rtl/0MjMxEjMxITM")
       


if __name__ == "__main__":
    app()
