from langchain_community.vectorstores import FAISS

from src.config import VECTOR_DB_PATH

def create_vector_store(chunks, embedding_model):

    db = FAISS.from_documents(
        chunks,
        embedding_model
    )

    db.save_local(VECTOR_DB_PATH)

    return db