import urllib

from myllm.MyApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.generate(

        model="dall-e-3",

        prompt="a white siamese cat versus black dog",

        size="1024x1024",

        quality="standard",

        n=1,

    )
    image_url = response.data[0].url
    print(image_url)
    imgName="img/dogcat.png"
    urllib.request.urlretrieve(image_url,  imgName)


if __name__ == "__main__":
    prompt="강아지하고 고양이하고 서로싸우는 이미지만드삼"
    test(prompt)