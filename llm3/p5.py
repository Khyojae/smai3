import time

import streamlit as st

from myLLM import geminiTxt

#side bar
st.sidebar.markdown("Clicked Page 5")

#page
st.title("Page 5")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
if st.button("SEND"):
    if text:
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------
        result = geminiTxt(text)
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문을 입력 하세요")



#------------------------------------
with st.container():
    st.write("이것은 컨테이너 내부입니다.")

    with st.expander("더 보기"):
        st.write("이곳에 추가 정보를 입력할 수 있습니다.")
    with st.expander("더 보기"):
        st.write("이곳에 추가 정보를 입력할 수 있습니다.")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Please enter your name")
        rating = st.slider("Please rate this app", 0, 10, 5)
    with col2:
        dob = st.date_input("Please enter your date of birth")
        recommend = st.radio("Would you recommend this app to others?", ("Yes", "No"))

    col1, col2, col3 = st.columns([3, 3, 3])

    with col1:
        st.header('Col1')
        st.image('https://static.streamlit.io/examples/cat.jpg',width=200)

    with col2:
        st.header('Col2')
        st.image('https://static.streamlit.io/examples/dog.jpg',width=200)

    with col3:
        st.header('Col3')
        st.image('https://static.streamlit.io/examples/owl.jpg',width=200)

    tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])
    with tab1:
        st.header('고양이')
        st.image('https://static.streamlit.io/examples/cat.jpg')

    with tab2:
        st.header('강아지')
        st.image('https://static.streamlit.io/examples/dog.jpg')

    with tab3:
        st.header('올빼미')
        st.image('https://static.streamlit.io/examples/owl.jpg')

    with st.expander("더 보기"):
        st.write("이곳에 추가 정보를 입력할 수 있습니다.")

    with st.expander("고양이 정보 보기"):
        st.write("여기에는 고양이에 대한 정보가 들어갑니다.")
        st.image('https://static.streamlit.io/examples/cat.jpg', width=200)
