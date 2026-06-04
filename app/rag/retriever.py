from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.rag.ingest import load_documents, split_documents
from app.config import EMBEDDING_MODEL

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

vectorstore = None


def create_vectorstore():

    print("Loading documents...")

    docs = load_documents()

    print("Splitting into chunks...")

    chunks = split_documents(docs)

    print(f"Creating embeddings for {len(chunks)} chunks...")

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    print("Vectorstore ready.")

    return vectorstore


def load_vectorstore():

    return FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )


def retrieve(query, k=3):

    global vectorstore

    if vectorstore is None:
        vectorstore = load_vectorstore()

    results = vectorstore.similarity_search_with_score(
        query,
        k=k
    )

    return results


if __name__ == "__main__":

    query = "What is the VPN timeout policy?"

    results = retrieve(query)

    for i, (doc, score) in enumerate(results):

        print("\n========================")
        print(f"RESULT {i+1}")
        print("========================")

        print(f"\nSCORE: {score}")

        print("\nMETADATA:")
        print(doc.metadata)

        print("\nCONTENT:")
        print(doc.page_content[:700])