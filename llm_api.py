from langchain_upstage import ChatUpstage
import os
import PyPDF2

# PDF에서 텍스트 추출
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            page_text = reader.pages[page].extract_text()
            page_text = page_text.replace('\n', ' ').replace('\r', ' ')
            text += page_text + ' '
    return ' '.join(text.split())

"""
@tool
def summarize_pdf_content(content):

    # 요약 
    return f"Summary of the content: {content[:500]}..."
"""

"""
tools = [summarize_pdf_content]
llm_with_tools = llm.bind_tools(tools)

def get_llm_response(content):

    messages = [
        {
            "role": "user",
            "content": f"Here is some text: {content[:1000]}... Can you summarize it using the provided tools?",
        }
    ]
    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        tool_call = response.tool_calls[0]
        function_name = tool_call["name"]
        function_to_call = summarize_pdf_content  # 도구 지정
        function_args = tool_call["args"]
        
        try:
            # invoke 
            function_response = function_to_call.invoke(**function_args)
        except KeyError:
            function_response = "Sorry, I couldn't process that content."
        
        return function_response
    
    print("No function calls were made. Attempting direct tool invocation.")
    return summarize_pdf_content.invoke(content)  # invoke 사용
    
"""

class LLMHandler:
    def __init__(self, api_key):
        self.llm = ChatUpstage(api_key=api_key)

    def ask_question_about_pdf(self, pdf_text, question):
        messages = [
            {"role": "system", "content": "You are a helpful assistant who knows the content of a PDF document."},
            {"role": "user", "content": f"Here is some text from a PDF: {pdf_text[:2000]}"},
            {"role": "user", "content": f"Based on the above context, please answer the following question: {question}"}
        ]
        return messages

    def call_llm(self, messages):
        response = self.llm.invoke(messages)
        return response.content  # response 에서 text 가져옴

    def get_response(self, context, question, chat_history=None):
        if chat_history:
            # 대화 히스토리가 있으면...
            formatted_history = "\n".join([f"User: {entry['user']}\nLLM: {entry['llm']}" for entry in chat_history])
            question = f"{formatted_history}\nUser: {question}"

        #print(f"(디버그) 최종 질문 메시지: {question}")  # 최종 질문 메시지

        messages = self.ask_question_about_pdf(context, question)
        
        #print(f"[디버깅] LLM에 보낼 메시지 구조: {messages}")  # LLM에 보낼 메시지 구조
        
        response = self.call_llm(messages)
        
        #print(f"[디버깅] LLM으로부터 받은 응답: {response}")  # LLM으로부터 받은 응답
        
        return response
