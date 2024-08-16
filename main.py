from llm_api import extract_text_from_pdf, LLMHandler
from file_loader import PDFLoader
from txt_splitter import SpliterModel
from vectorstore import create_vector_store
from retriever import Retriever
from langchain_upstage import UpstageEmbeddings
import os
from chat_log import ChatLog  # ChatLog


def main():
    # API 키 가져오기
    api_key = os.getenv("UPSTAGE_API_KEY")
    
    if not api_key:
        print("API 키가 설정되지 않았습니다.")
        return
    
    # LLMHandler 초기화
    llm_handler = LLMHandler(api_key)

    # UpstageEmbeddings 초기화
    embeddings = UpstageEmbeddings(
        api_key=api_key,
        model="solar-embedding-1-large-passage"
    )

    # ChatLog 초기화
    chat_log = ChatLog(max_length=20)

    # PDF 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, "data", "올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf")

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
    retriever = Retriever(vector_store, embeddings)
    
    #loop
    while True:
        # 질문 입력
        question = input("PDF 내용에 대해 질문하세요 (종료하려면 'exit' 입력): ")
        if question.lower() == "exit":
            print("종료합니다.")
            break

        # 검색 및 답변 생성
        search_results = retriever.retrieve(question)
        if not search_results:
            print("관련된 문서를 찾을 수 없습니다.")
            continue

        context = search_results[0].page_content  # 첫 번째 검색 결과 사용

        answer = llm_handler.get_response(context, question, chat_log.chat_history)
        
        if answer is None:
            print("[에러] LLM으로부터 응답을 받지 못했습니다.")
            continue
        # LLM 응답 출력
        
        print("\n답변:")
        print(answer)    
        
         # 채팅 로그에 추가
        chat_log.add_to_log(question, answer)
         # 필요시 로그를 파일에 저장
        chat_log.save_log_to_file('chat_history.json')


if __name__ == "__main__":
    main()
