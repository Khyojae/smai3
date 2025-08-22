import urllib

import streamlit as st
from PIL import Image

from myLLM import save_uploadedfile, geminiModel, progressBar, save_carpturefile, encode_image, openAiModel, makeAudio

def test(prompt):
    openModel = openAiModel()
    response1 = openModel.images.create_variation(

        model="dall-e-2",

        image=open(prompt, "rb"),

        n=3,

        size="1024x1024"

    )
    for n, data in enumerate(response.data):
        print(data.url)
        name = f"temp_{n}.png"
        urllib.request.urlretrieve(data.url, name)

# Sidebar
st.sidebar.markdown("Clicked Page 5")

# Page
st.title("Page 5")
picture = st.camera_input("Take a picture")

if picture:
    st.info("이미지를 캡쳐햇5")
    save_carpturefile("img/",picture,"temp.png",st)
    text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
    if st.button("SEND"):
        base64img = encode_image("img/temp.png")
        model = openAiModel()
        my_bar = progressBar("Operation in progress. Please wait.")
        response = model.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": "당신은 한국인이고, 친절하고 꼼꼼한 서포터 입니다. 질문에 정성을 다해 답변합니다."},
                {"role": "user", "content": [
                    {"type": "text", "text": text},
                    {"type": "image_url", "image_url": {
                        "url": f"data:image/jpg;base64,{base64img}"}
                     }
                ]}
            ],
            temperature=0.0,
        )
        my_bar.empty()

# 결과를 출력하고
# 음성으로 안내한다
        result = response.choices[0].message.content
        st.success(result)
        makeAudio(result, "result.mp3")
        st.audio("audio/result.mp3", autoplay=True)



    else:
        st.warning("질문을 입력하세요.")
