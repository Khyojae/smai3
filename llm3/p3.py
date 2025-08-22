import time

import streamlit as st
from myLLM import geminiTxt
from myLLM import progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 3")

# Page
st.title("Page 3 프로그램 작성기")
text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")

selected_option = st.radio("언어를 선택하세요", ("짜바", "파이썬", "씨쁠쁠"))


if st.button("SEND"):
    if text and selected_option:
        st.write(f"선택된 옵션: {selected_option}")
        st.info(text)
        my_bar=progressBar("ㄱㄷ")
        result=geminiTxt(f"{selected_option}으로 질문을 코딩해줘");
        my_bar.empty()
        st.code(result,language=selected_option)

    else:
        st.info("쓰3")