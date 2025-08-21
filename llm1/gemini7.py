from io import BytesIO

import requests
from PIL import Image

from myllm.MyApi import geminiModel


def test(prompt,img):
    model = geminiModel()
    response = model.generate_content([prompt,img])
    print(response.text)

if __name__ == "__main__":
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlPneVmULIy154ZgXoMbsqCO2oqC127EbFcg&s"
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt = "이 이미지의 성분을 알려줘"
    test(prompt,img)