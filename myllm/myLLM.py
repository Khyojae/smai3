from openai import chat  # 이 임포트는 불필요할 수 있음
from myllm.MyApi import geminiModel


def test(txt):
    model = geminiModel()
    response = model
    return response.text