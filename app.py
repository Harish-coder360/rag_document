# Directory: llm_rag/

# -----------------------------
# File: app.py
# -----------------------------
import gradio as gr
import os
import tempfile
from rag import answer_query
from langchain_community.document_loaders import TextLoader, PDFMinerLoader, UnstructuredMarkdownLoader, UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from vector_store import get_vectorstore
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def process_uploaded_file(uploaded_file_path):
    ext = os.path.splitext(uploaded_file_path)[-1].lower()

    if ext == ".txt":
        loader = TextLoader(uploaded_file_path)
    elif ext == ".pdf":
        loader = PDFMinerLoader(uploaded_file_path)
    elif ext == ".md":
        loader = UnstructuredMarkdownLoader(uploaded_file_path)
    elif ext == ".docx":
        loader = UnstructuredWordDocumentLoader(uploaded_file_path)
    else:
        raise ValueError("Unsupported file format. Please upload .txt, .pdf, .md, or .docx")

    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def query_llm(user_api_key, user_query, uploaded_file):
    if not user_api_key:
        return "Please enter your OpenAI API key."
    if not user_query:
        return "Please enter a query."
    if not uploaded_file:
        return "Please upload a document file."

    try:
        suffix = os.path.splitext(uploaded_file.name)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            with open(uploaded_file.name, 'rb') as source:
                tmp.write(source.read())
            tmp.flush()
            documents = process_uploaded_file(tmp.name)

        embedder = OpenAIEmbeddings(openai_api_key=user_api_key)
        vectorstore = get_vectorstore(embedder)
        vectorstore.add_documents(documents)
        retriever = vectorstore.as_retriever()

        llm = ChatOpenAI(api_key=user_api_key)
        rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        return rag_chain.run(user_query)

    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(title="RAG Assistant") as demo:
    gr.Markdown("""
    <div style="text-align: center; font-family: 'Segoe UI', sans-serif;">
        <h1 style="color: #3b82f6; font-weight: bold;">🤖 Retrieval-Augmented Generation Assistant</h1>
        <p style="font-size: 1.1rem; color: #555;">Upload a document, ask a question, and get intelligent answers powered by LLMs.</p>
    </div>
    """)

    with gr.Row():
        user_api_key = gr.Textbox(label="🔐 OpenAI API Key", type="password", placeholder="sk-...", scale=1)

    with gr.Row():
        user_query = gr.Textbox(label="💬 Your Query", placeholder="e.g., What is this document about?", lines=2, scale=1)

    with gr.Row():
        uploaded_file = gr.File(label="📁 Upload Document (.txt, .pdf, .md, .docx)", file_types=['.txt', '.pdf', '.md', '.docx'], scale=1)

    with gr.Row():
        output = gr.Textbox(label="📜 Answer", lines=6)

    with gr.Row():
        submit = gr.Button("🔎 Generate Answer", variant="primary")

    submit.click(fn=query_llm, inputs=[user_api_key, user_query, uploaded_file], outputs=output)

demo.launch(share=True)