# retriver_Qa chain
from langchain.chains import RetrievalQA

def create_qa_chain(llm, retriever):

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    return qa_chain