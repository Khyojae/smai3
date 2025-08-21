from myllm.MyApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test(prompt):
    modelName="gpt-4o"
    msg=makeMsg("너는 친절한 한국 선생",prompt)
    result= openAiModelArg(modelName,msg)
    print(result)

if __name__ == "__main__":
    prompt="의 수도가 어디야"
    test(prompt)