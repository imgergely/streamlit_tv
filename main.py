import streamlit as st
import streamlit.components.v1 as components


def app():
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        tv2 = st.button("TV2")
    with col2:
        rtl = st.button("RTL")
    with col3:
        filmplusz = st.button("FILM+")
    with col4:
        zenebutik = st.button("ZENEBUTIK")

    if tv2:
        st.video("https://cdn.mediaklikk.org:443/tv2/0MjMxEjMxITM")
    if rtl:
        st.video("https://cdn.mediaklikk.org:443/rtl/0MjMxEjMxITM")
    if filmplusz:

        components.html(
        """
        <script src="https://cdn.jsdelivr.net/npm/hls.js@1"></script>

        <video id="video"></video>
        <script>
        var video = document.getElementById('video');
        var videoSrc = 'https://hls25.sweet.tv/stream/zxzaan6u3giy62guu8xikhvw89ybr2hui8t94qga5424feqkjmg9jq2xd7nfjxyd8yip3qfbkznmwpwqq2qx73tuyndkg3kzm84y4jdvhv4y65wnisr56ujigvtq95upn67xahubcbj9vi5sqe======.m3u8';
        if (Hls.isSupported()) {
            var hls = new Hls();
            hls.loadSource(videoSrc);
            hls.attachMedia(video);
        }

        else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = videoSrc;
        }
        </script>

        """,
        height=600,
        )
   
if __name__ == "__main__":
    app()

