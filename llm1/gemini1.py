from openai import chat  # 이 임포트는 불필요할 수 있음
from myllm.MyApi import geminiModel


def start_chat_session():
    model = geminiModel()
    chat_session = model.start_chat(history=[])
    return chat_session


def test(chat_session, txt):
    if txt == "q":
        return None
    response = chat_session.send_message(txt)
    return response.text


if __name__ == "__main__":
    chat_session = start_chat_session()

    while True:
        txt = input("질문을 입력(q): ")
        if txt == "q":
            print("종료")
            break
        result = test(chat_session, txt)
        print(result)

    # 대화 이력 출력
    print("\n대화 히스토리:")
    for message in chat_session.history:
        print(f"{message.role}: {message.parts[0].text}")
