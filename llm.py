from langchain_upstage import ChatUpstage 

class LlmModel():
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        
    def UpstageModel(self):
        
        llm = ChatUpstage(api_key= self.api_key, model_name="solar-1-mini-chat")
        return llm