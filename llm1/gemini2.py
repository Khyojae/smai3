from PIL import Image

from myllm.MyApi import geminiModel


def test():
    img=Image.open("img/cha.jpg")
    model = geminiModel()
    response = model.generate_content(["이사람 누구임",img])
    print(response.text)

if __name__ == "__main__":
    test()