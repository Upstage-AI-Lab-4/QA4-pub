from langchain_community.document_loaders import PyMuPDFLoader

class PDFLoader():
    def __init__(self, path) -> None:
        self.path = path
        
    def FileLoader(self):
        loader = PyMuPDFLoader(self.path).load()
        return loader