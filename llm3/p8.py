import streamlit as st

from myLLM import save_uploadedfile, makeAudio

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
text = st.text_input("질문 입력", placeholder="질문을 입력하세요")
if st.button("SEND"):
    if text:
        st.info(text)
        makeAudio(text, "temp.mp3")
        #음성으로 플레이
        #openai 물어보고 결과를 받는다
    else:
        st.audio("audio/retry.mp3", autoplay=True, width=1)
        st.info("입력 하세요")