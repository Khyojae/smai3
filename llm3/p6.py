import streamlit as st
from PIL import Image

from myLLM import save_uploadedfile, geminiModel, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 5")







# Page
st.title("Page 6 File Upload")
menu=st.selectbox("파일 타입 선택",["IMAGE","PDF","CSV"])
picture = st.camera_input("Take a picture")


if menu=="IMAGE":
    st.subheader(menu)
    file=st.file_uploader("이미지를 선택",type=["ipg","png","jpeg"])
    if file:
        save_uploadedfile("img",file,st)
        st.download_button(
            label="파일다운로드",
            data=file,
            file_name=file.name,
            mime="image/jpg"
        )

elif menu=="PDF":
    st.subheader(menu)
    file = st.file_uploader("pdf를 선택", type=["pdf"])
    if file:
        save_uploadedfile("pdf", file, st)
        st.download_button(
            label="파일다운로드",
            data=file,
            file_name=file.name,
            mime="application/pdf"
        )
elif menu=="CSV":
    st.subheader(menu)
    file = st.file_uploader("csv를 선택", type=["csv"])
    if file:
        save_uploadedfile("csv", file, st)
        st.download_button(
            label="파일다운로드",
            data=file,
            file_name=file.name,
            mime="text/text"
        )





