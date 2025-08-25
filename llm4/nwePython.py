from langchain_core.prompts import PromptTemplate


def test(txt):
    template = "txt를 홍보하기 위한 문구를 만들어줘"
    prompt = PromptTemplate(
    input_variables=["product"],
    template=template
    )
    print(prompt.format(product=txt))


if __name__ == "__main__":
     test("카메라")
