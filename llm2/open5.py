from myllm.MyApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.generate(

        model="dall-e-3",

        prompt="a white siamese cat and black dog",

        size="1024x1024",

        quality="standard",

        n=1,

    )
    image_url = response.data[0].url
    print(image_url)

if __name__ == "__main__":
    prompt="카와이"
    test(prompt)