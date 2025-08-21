from myllm.MyApi import openAiModel, openAiModelArg, makeMsg


def test():
    model=openAiModel()
    response = openAiModelArg("gpt-4o",makeMsg("한국 선생님","천안 신방동에 맛집 알려줘"))
    print(response)


if __name__ == "__main__":
    test()
