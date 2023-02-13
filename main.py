import streamlit as st
import streamlit.components.v1 as components


def app():
    
    col1, col2 = st.columns(2)
    with col1:
        tv2 = st.button("TV2")
    with col2:
        rtl = st.button("RTL")

    if tv2:
        st.video("https://cdn.mediaklikk.org:443/tv2/0MjMxEjMxITM")
    if rtl:
        st.video("https://cdn.mediaklikk.org:443/rtl/0MjMxEjMxITM")

if __name__ == "__main__":
    app()

