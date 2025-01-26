import streamlit as st
from dotenv import load_dotenv
from embeddings import vector_embedding
from retriever import retrieve_answer
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq  # Importing the LLM for query processing

import os

# Load environment variables
load_dotenv()

# Access API keys
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")

# Set Streamlit page configuration with a theme
st.set_page_config(
    page_title="TrackIt Chatbot", 
    page_icon="🛒", 
    layout="wide",  # Allows more space for both main content and the sidebar
    initial_sidebar_state="expanded"
)

# Custom CSS for colorful styling
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue background */
        color: #333333;            /* Text color */
    }
    .stButton button {
        background-color: #15803D; /* dark green button */
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
    .stTextInput > div > input {
        border: 2px solid #4caf50;
        border-radius: 8px;
        font-size: 16px;
    }
    .main-header {
        color: #15803D; /* dark green button */
        text-align: center;
        font-size: 2.2rem;
    }
    .chat-history {
        border: 1px solid #4caf50;
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        font-size: 1rem;
        max-height: 400px;
        overflow-y: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Main App Header
st.markdown('<h1 class="main-header"> TrackIt - Student Query Chatbot </h1>', unsafe_allow_html=True)
st.markdown("""
    <div style="background-color: #000000; padding: 15px; border-radius: 10px; font-size: 1.1rem; color: white;">
         Welcome to the <strong>TrackIt - Student Query Chatbot</strong>!  Get instant answers to your questions about attendance, performance, and academic details effortlessly. 😊
    </div>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Sidebar for Chat History
with st.sidebar:
    st.markdown("<h2 style='color: #4caf50;'>📝 Chat History</h2>", unsafe_allow_html=True)
    if st.session_state.conversation_history:
        st.markdown('<div class="chat-history">', unsafe_allow_html=True)
        for message in st.session_state.conversation_history:
            st.markdown(f"""
                <p><b>User:</b> {message['user']}</p>
                <p><b>Bot:</b> {message['bot']}</p>
                <hr style="border: none; border-top: 1px solid #ddd;">
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("No chat history available.")

# Vector embedding initialization
if "vectors" not in st.session_state:
    vector_embedding()

# User Query Input
st.markdown("<h2 style='color: #333333;'>🔎 Ask a question:</h2>", unsafe_allow_html=True)
user_query = st.text_input("", placeholder="e.g., 'What is the CGPA of Student X?'")

# Search Button
search_button = st.button("✨ Search")

# Response Display and Chat History Update
if user_query and search_button:
    with st.spinner('⏳ Processing your query...'):
        if "vectors" not in st.session_state:
            st.error("❌ Vector store not initialized.")
        else:
            # Define the prompt template
           
            prompt = ChatPromptTemplate.from_template("""
        Answer the questions based on the context provided:
    {context}
    
    {input}
""")


            # Call retrieve_answer with all required arguments
            response = retrieve_answer(llm, st.session_state.vectors, prompt, user_query)
            
            # Save query and response to chat history
            st.session_state.conversation_history.append({"user": user_query, "bot": response})
            
            # Display the bot response
            st.markdown(f"""
                <div style="background-color: #000000; padding: 15px; border-radius: 10px; margin-top: 20px; font-size: 1.1rem; color: white;">
                    <b>Bot:</b> {response}
                </div>
            """, unsafe_allow_html=True)

# Sidebar with additional info
st.sidebar.markdown("""
    <h3 style="color: #4caf50;">💡 How to Use:</h3>
    <ul>
        <li>Enter a question about a student or academic data.</li>
        <li>Click "Search" to get instant answers!</li>
    </ul>
    <h3 style="color: #4caf50;">📈 TrackIt Features:</h3>
    <p>- Easy performance tracking<br>- Attendance details at your fingertips<br>- AI-powered answers</p>
""", unsafe_allow_html=True)
