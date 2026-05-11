from transformers import pipeline

from langchain_huggingface import HuggingFacePipeline

from src.config import LLM_MODEL

def load_llm():

    pipe = pipeline(
        "text-generation",
        model=LLM_MODEL,
        max_new_tokens=200
    )

    llm = HuggingFacePipeline(
        pipeline=pipe
    )

    return llm