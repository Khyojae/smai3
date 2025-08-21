from myllm.MyApi import geminiModel, openAiModel, openAiModelArg, makeMsg


def test(prompt):
    modelName="gpt-4o"
    msg=makeMsg("너는 10문장으로 말하는 사람이야",prompt)
    result= openAiModelArg(modelName,msg)
    print(result)

if __name__ == "__main__":
    prompt="sk 하이닉스에 대해서 알려줘 "
    test(prompt)