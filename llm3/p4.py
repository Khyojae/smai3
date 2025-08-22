import time

import streamlit as st
from myLLM import geminiTxt, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 4")

# Page
st.title("Page 4 번역기")
text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
language = st.selectbox("언어를 선택하시오", ["Eng", "Jap", "Kor"])

if st.button("send"):
    if text and language:
        st.info(f"선택하신 언어는{language}")
        st.info(text)
        my_bar = progressBar("ㄱㄷ")
        result = geminiTxt(f"{language}으로 질문을 코딩해줘");
        my_bar.empty()
        st.code(result, language=language)
    else:
        st.info(f"선택한 언어: {language}")

