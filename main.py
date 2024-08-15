import sys
import os
from llm_api import extract_text_from_pdf, LLMHandler
from file_loader import PDFLoader
from txt_splitter import SpliterModel
from vectorstore import create_vector_store

def main():
    # API 키 가져오기
    api_key = os.getenv("UPSTAGE_API_KEY")
    
    if not api_key:
        print("API 키가 설정되지 않았습니다.")
        return
    
    # LLMHandler 초기화
    llm_handler = LLMHandler(api_key)
    
    # 인코딩 문제 해결 -> utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    # PDF 파일 경로 설정
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, r"data\올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf")

    # 경로 확인
    if not os.path.exists(pdf_path):
        print(f"파일을 찾을 수 없습니다: {pdf_path}")
        return

    # PDF 텍스트 추출
    pdf_text = extract_text_from_pdf(pdf_path)
    
    # PDF 로딩
    docs = PDFLoader(pdf_path).FileLoader()
    
    # 텍스트 분할
    split_documents = SpliterModel('RecursiveCharacter', docs).split_text()
    
    # 벡터 저장소 생성
    chroma_db = create_vector_store(split_documents)
        
    # 사용자 질문 입력
    question = input("PDF 내용에 대해 질문하세요: ")
    
    # 질문에 대한 답변 생성
    answer = llm_handler.get_response(pdf_text, question)
    
    # 답변 출력
    print("\n답변:")
    print(answer)

if __name__ == "__main__":
    main()
