import sys
from llm_api import extract_text_from_pdf, get_response
from file_loader import PDFLoader
from txt_splitter import SpliterModel
from prompt import PromptQaChat
from conversational_rag import ConversationalRAGChain

### Statefully manage chat history ###
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory


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
    
    # QA
    question = input()
    response = ConversationalRAGChain(rag_chain, question).chain()
    print(response["answer"])
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