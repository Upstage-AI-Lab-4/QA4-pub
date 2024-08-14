from langchain_upstage import ChatUpstage
from langchain.tools import tool
import os
import PyPDF2

#file extract
def extract_text_from_pdf(pdf_path):
 
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            page_text = reader.pages[page].extract_text()
            
            page_text = page_text.replace('\n', ' ')
            page_text = page_text.replace('\r', ' ')
            
            text += page_text + ' '
            
    text = ' '.join(text.split())
    return text
"""
@tool
def summarize_pdf_content(content):

    # 요약 
    return f"Summary of the content: {content[:500]}..."
"""

# LLM 설정
llm = ChatUpstage(api_key=os.getenv("UPSTAGE_API_KEY"))
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

def ask_question_about_pdf(pdf_text, question):
    messages = [
        {"role": "system", "content": "You are a helpful assistant who knows the content of a PDF document."},
        {"role": "user", "content": f"Here is some text from a PDF: {pdf_text[:2000]}"},
        {"role": "user", "content": f"Based on the above context, please answer the following question: {question}"}
    ]
    
    return messages

def call_llm(messages):

    response = llm.invoke(messages)
    return response.content  # response 에서 text 가져옴

#ask_questions_about_pdf + call_llm / 전체 관리 function
def get_response(context, question):

    messages = ask_question_about_pdf(context, question)
    response = call_llm(messages)
    return response