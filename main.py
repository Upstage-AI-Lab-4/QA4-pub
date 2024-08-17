import sys
import os
# from llm_api import LLMHandler
from llm import LlmModel
from file_loader import PDFLoader
from txt_splitter import SpliterModel
from vectorstore import create_vector_store
from retriever import Retriever
from langchain_upstage import UpstageEmbeddings
from prompt import PromptQaChat
from conversational_rag import ConversationalRAGChain
from chat_log import ChatLog  # ChatLog

def main():
    # API 키 가져오기
    
    os.environ["UPSTAGE_API_KEY"] = 'UPSTAGE_API_KEY'
    api_key = os.getenv("UPSTAGE_API_KEY")
    
    if not api_key:
        print("API 키가 설정되지 않았습니다.")
        return
    
    # LLMHandler 초기화
    llm = LlmModel(api_key).UpstageModel()

    # UpstageEmbeddings 초기화
    embeddings = UpstageEmbeddings(
        api_key=api_key,
        model="solar-embedding-1-large-passage"
    )


    # 인코딩 문제 -> utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    # PDF 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, "data", "올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf")
    
    # 경로 확인
    if not os.path.exists(pdf_path):
        print(f"파일을 찾을 수 없습니다: {pdf_path}")
        return

    # PDF 텍스트 추출 및 로딩
    pdf_loader = PDFLoader(pdf_path)
    docs = pdf_loader.FileLoader()
    
    if not docs:
        print("PDF 로드에 실패했습니다.")
        return
    
    # 텍스트 분할
    split_model = SpliterModel('RecursiveCharacter', docs)
    split_documents = split_model.split_text()

    # 벡터 저장소
    vector_store = create_vector_store(split_documents)
    
    if vector_store is None:
        print("벡터 스토어 생성에 실패했습니다.")
        return
    
    # 리트리버 초기화 및 embeddings 전달
    retriever = Retriever(vector_store).retrieve()

    # Chain with chat history, prompt
    rag_chain = PromptQaChat(llm, retriever).promptChain()
    

    while True:
    # for i in range(2):
        # 질문 입력
        question = input("PDF 내용에 대해 질문하세요 (종료하려면 'exit' 입력): ")
        if question.lower() == "exit":
            print("종료합니다.")
            break

        # 검색 및 답변 생성
        response = ConversationalRAGChain(rag_chain, question).chain()
        answer = str(response["answer"])
        
        if answer is None:
            print("[에러] LLM으로부터 응답을 받지 못했습니다.")
            continue
        
        # LLM 응답 출력
        print("\n답변:")
        print(answer)    
        
         # 채팅 로그에 추가
        ChatLog.add_to_log( question, answer)
         # 필요시 로그를 파일에 저장
        ChatLog.save_log_to_file('chat_history.json')
        
        
if __name__ == "__main__":
    main()
