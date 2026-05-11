from langchain_community.embeddings import HuggingFaceEmbeddings

from src.config import EMBEDDING_MODEL

def load_embeddings():

    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embedding_model