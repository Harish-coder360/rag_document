from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_documents(directory_path: str, chunk_size: int = 500, chunk_overlap: int = 50):
    loader = DirectoryLoader(directory_path, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)