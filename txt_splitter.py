from langchain_text_splitters import RecursiveCharacterTextSplitter

class SpliterModel():
    def __init__(self, model_name, docs) -> None:
        self.model_name = model_name
        self.docs = docs
        
    def split_text(self):
        # if self.model_name == 'RecursiveCharacter':
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(self.docs)
        return text_splitter
