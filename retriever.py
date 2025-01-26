# retriever.py

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def retrieve_answer(llm, vectors, prompt, query):
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(vectors.as_retriever(), document_chain)

    response = retrieval_chain.invoke({'input': query})
    return response['answer']
