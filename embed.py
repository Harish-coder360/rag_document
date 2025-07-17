from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from config import Config


def get_embedder():
    if Config.EMBEDDING_MODEL == "openai":
        return OpenAIEmbeddings()
    else:
        return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")