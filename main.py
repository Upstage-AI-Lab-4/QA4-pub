import sys
from llm_api import extract_text_from_pdf, get_response
from file_loader import PDFLoader
from txt_splitter import SpliterModel
from prompt import PromptQaChat

### Statefully manage chat history ###
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

def main():
    # PDF file
    pdf_path = "올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf"

    # PDF text 추출
    pdf_text = extract_text_from_pdf(pdf_path)
    """
    # LLM 요청
    summary = get_llm_response(pdf_text)
    """
    
    
    # loader
    docs = PDFLoader(pdf_path).FileLoader()
    
    # text_splitter
    split_documents = SpliterModel('RecursiveCharacter', docs).split_text()
    
    
    
    # Chain with chat history, prompt
    rag_chain = PromptQaChat(llm, retriever).promptChain()
    
    
    ### Statefully manage chat history ###
    # ChatMessageHistory가 휘발성이라 main에서 관리
    # https://python.langchain.com/v0.1/docs/use_cases/question_answering/chat_history/#chain-with-chat-history
    store = {}
    def get_session_history(session_id: str) -> BaseChatMessageHistory:
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
    )
    
    question = input()
    
    response = conversational_rag_chain.invoke(
        {"input": {question}},
        config={
            "configurable": {"session_id": "abc123"}
        },  # constructs a key "abc123" in `store`.
        )["answer"]
    print(response)
    # KeyError('answer')는 langchain오류라고 함
    

    # 인코딩 문제 -> utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    question = input("PDF 내용에 대해 질문하세요: ")
    answer = get_response(pdf_text, question)
    
    # 답변 출력
    print("\n답변:")
    print(answer)

    """
    # 요약
    print(summary)
    """

if __name__ == "__main__":
    main()