from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents
# TESTING

# docs = load_pdf()

# print("Total Pages:", len(docs))

# print("\nFirst Page Content:\n")

# print(docs[0].page_content)

# print("\nMetadata:\n")

# print(docs[0].metadata)
