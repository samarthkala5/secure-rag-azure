from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

DOCUMENTS_PATH = "documents"


def load_documents():
    documents = []

    for file in sorted(os.listdir(DOCUMENTS_PATH)):

        path = os.path.join(DOCUMENTS_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
            continue

        if file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            documents.extend(loader.load())

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    docs = load_documents()

    print(f"Loaded {len(docs)} pages")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    print("\n===== SAMPLE CHUNK =====\n")

    print(chunks[0].page_content[:500])

    print("\n===== METADATA =====\n")

    print(chunks[0].metadata)