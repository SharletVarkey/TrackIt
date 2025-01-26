# embeddings.py

import os
import pandas as pd
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document



def vector_embedding():
    if "vectors" not in st.session_state:
        model_name = "models/embedding-001"
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model=model_name)

        csv_directory = r"./"  # Directory for CSVs
        csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]
        if not csv_files:
            st.error("No CSV files found.")
            return

        st.session_state.docs = []
        for csv_file in csv_files:
            df = pd.read_csv(os.path.join(csv_directory, csv_file))
            for _, row in df.iterrows():
                content = f"Name: {row['Student Name']}\nID: {row['Student ID']}\nAttendance: {row['Overall Attendance']}\nCGPA: {row['Overall CGPA']}\nPython: {row['Python']}\nBig data: {row['Big data']}\nDBMS: {row['DBMS']}\nAI: {row['AI']}\nPython attendance: {row['Python Attendance']}\nBig data attendance: {row['Big data Attendance']}\nDBMS attendance: {row['DBMS Attendance']}\nAI attendance: {row['AI Attendance']}"
                st.session_state.docs.append(Document(page_content=content, metadata={"source": csv_file}))

        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)

        if st.session_state.final_documents:
            st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
            st.success("Embeddings and vector store initialized.")
