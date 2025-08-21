import time

import streamlit as st
from myLLM import geminiModel, geminiTxt


def test(prompt):
    model = geminiModel()
    response = model.generate_content(prompt)
    print(response.text)

#side bar
st.sidebar.markdown("Clicked Page 3")

#page
st.markdown("Page 3 프로그램 작성기")
text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
selected_option =st.radio("옵션을 선택하시오:",["c++","python","java"],index=0)
if st.button("SEND"):
    if text:
        language_instruction=f"{selected_option}로 답변해줘."
        full_prompt = language_instruction+text
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------
        result = geminiTxt(full_prompt)
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")


