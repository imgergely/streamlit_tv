import streamlit as st
import streamlit.components.v1 as components


def app():
    
    col1, col2 = st.columns(2)
    with col1:
        tv2 = st.button("TV2")
    with col2:
        rtl = st.button("RTL")

    if tv2:
        components.html(
        """
        <video controls autoplay="true" id="video">
        <source 
            src="https://cdn.mediaklikk.org:443/tv2/0MjMxEjMxITM" 
            type="video/mp4" />
        </video>
        """,
        height=1754,
        width=1240)
        
    if rtl:
        components.html(
        """
        <video controls autoplay="true" id="video">
        <source 
            src="https://cdn.mediaklikk.org:443/rtl/0MjMxEjMxITM" 
            type="video/mp4" />
        </video>
        """,
        height=1754,
        width=1240)

if __name__ == "__main__":
    app()

