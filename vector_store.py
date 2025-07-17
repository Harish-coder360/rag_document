from langchain.vectorstores import Chroma, FAISS
from config import Config

def get_vectorstore(embedding_function, persist_directory="vector_store"):
    if Config.VECTOR_STORE == "chromadb":
        return Chroma(embedding_function=embedding_function, persist_directory=persist_directory)
    else:
        return FAISS(embedding_function=embedding_function)