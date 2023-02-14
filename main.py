import streamlit as st
import streamlit.components.v1 as components


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
        run("https://cdn.mediaklikk.org:443/tv2/0MjMxEDMxQTM")
       
    if rtl:
        run("https://cdn.mediaklikk.org:443/rtl/0MjMxEDMxQTM")

    if ujra:
        st.experimental_rerun()

if __name__ == "__main__":
    app()
