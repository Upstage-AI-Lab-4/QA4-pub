import sys
import os
from llm_api import extract_text_from_pdf, LLMHandler
from file_loader import PDFLoader
from txt_splitter import SpliterModel

def main():
    
    api_key = os.getenv("UPSTAGE_API_KEY")
    
    llm_handler = LLMHandler(api_key)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, "data", "올림픽예선시리즈 스포츠클라이밍_ 필수 정보.pdf")

    # 경로 확인
    if not os.path.exists(pdf_path):
        print(f"파일을 찾을 수 없습니다: {pdf_path}")
        return

    # PDF text 추출
    pdf_text = extract_text_from_pdf(pdf_path)
    """
    # LLM 요청
    summary = get_llm_response(pdf_text)
    """
    
    # loader
    docs = PDFLoader(pdf_path).FileLoader().load()
    
    # text_splitter
    split_documents = SpliterModel('RecursiveCharacter', docs).split_text()
    
    
    # 인코딩 문제 -> utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    question = input("PDF 내용에 대해 질문하세요: ")
    answer = llm_handler.get_response(pdf_text, question)
    
    # 답변 출력
    print("\n답변:")
    print(answer)

    """
    # 요약
    print(summary)
    """

if __name__ == "__main__":
    main()