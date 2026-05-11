import streamlit as st

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import load_embeddings
from src.vector_store import create_vector_store
from src.retriever import create_retriever
from src.llm_model import load_llm
from src.qa_chain import create_qa_chain

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Research Paper Assistant",
    layout="wide"
)

st.title("AI Research Paper Assistant")

st.write(
    "Upload a research paper PDF and ask questions."
)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# CACHE MODELS
# -----------------------------------

@st.cache_resource
def get_embedding_model():
    return load_embeddings()

@st.cache_resource
def get_llm_model():
    return load_llm()

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Research Paper",
    type="pdf"
)

# -----------------------------------
# PROCESS PDF
# -----------------------------------

if uploaded_file is not None:

    # Save uploaded PDF

    with open("data/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded Successfully")

    # Only process once

    if st.session_state.qa_chain is None:

        with st.spinner("Processing Research Paper..."):

            # LOAD PDF

            documents = load_pdf("data/temp.pdf")

            # SPLIT DOCUMENTS

            chunks = split_documents(documents)

            # LOAD EMBEDDINGS

            embedding_model = get_embedding_model()

            # CREATE VECTOR STORE

            db = create_vector_store(
                chunks,
                embedding_model
            )

            # CREATE RETRIEVER

            retriever = create_retriever(db)

            # LOAD LLM

            llm = get_llm_model()

            # CREATE QA CHAIN

            qa_chain = create_qa_chain(
                llm,
                retriever
            )

            # STORE QA CHAIN

            st.session_state.qa_chain = qa_chain

        st.success("Research Paper Ready for Questions")

# -----------------------------------
# CHAT INTERFACE
# -----------------------------------

if st.session_state.qa_chain is not None:

    query = st.chat_input(
        "Ask a question about the paper..."
    )

    if query:

        # Store user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": query
            }
        )

        # Generate response

        with st.spinner("Generating Answer..."):

            response = st.session_state.qa_chain.run(query)

        # Store assistant message

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

# -----------------------------------
# DISPLAY CHAT
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])