




# TrackIt - Student Query Chatbot

📚 **TrackIt** is an AI-powered chatbot designed to query and retrieve information from student data, including attendance and academic performance. It processes custom-made datasets to provide answers to queries about student data. Currently, the project supports querying student data, with future plans to include staff and administrators.

## Features

- **Student Data Querying**: Allows users to query information about student attendance, performance, and other academic details.
- **AI-Powered Responses**: The chatbot leverages Google Generative AI to provide answers based on the provided student dataset.
- **Interactive Interface**: Built using Streamlit, offering a user-friendly chat interface where users can ask questions and view responses.
- **Future Expansion**: In the future, the chatbot will support querying data from staff and administrators in addition to students.

## Technologies Used

- **Streamlit**: For creating a user-friendly and interactive web interface.
- **Pandas**: For handling and processing student data.
- **LangChain**: To manage the query classification and integrate LLMs for generating answers.
- **LangChain-Google-GenAI**: For embedding student data using Google Generative AI.
- **Dotenv**: To securely manage and load API keys for external services.

## How It Works

1. **Data Handling**: The project processes student data from CSV files containing details like student IDs, academic performance, and attendance.
2. **Embedding Generation**: The student data is converted into embeddings using Google Generative AI, which are stored in a FAISS vector database.
3. **Query Classification**: The user's query is classified based on keywords, and a relevant answer is retrieved from the dataset.
4. **Response Generation**: The chatbot uses a retrieval chain to generate contextually relevant responses based on the dataset and the user's query.

## Setup and Installation

### Requirements

- Python 3.8+
- Install dependencies:
  
  ```bash
  pip install -r requirements.txt
  ```

- **API Keys**: Set up your API keys for Groq AI and Google Generative AI in the `.env` file:

  ```bash
  GROQ_API_KEY=your_groq_api_key
  GOOGLE_API_KEY=your_google_api_key
  ```

### Running the Application

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/trackit.git
   cd trackit
   ```

2. **Run the App**:

   ```bash
   python main.py
   ```

3. Open the app at `http://localhost:7860` to interact with the chatbot.

### Future Features

- **Support for Staff and Administrators**: In future updates, the project will support querying data for staff and administrators of the department.
- **Real-Time Analysis**: Real-time data analysis and querying will be added in future versions of the application.

## File Overview

- **classifier_query.py**: Classifies user queries based on keywords.
- **embeddings.py**: Processes student data, generates embeddings, and stores them in a FAISS vector database.
- **main.py**: The main Streamlit app that allows querying student data and displays responses.
- **retrieve.py**: Retrieves answers from the vector store based on user queries.
- **test.py**: Handles secret key management via the `.env` file.
- **utils.py**: Manages chat history display within the Streamlit app.
- **.env**: Contains sensitive API keys for Groq AI and Google Generative AI.

## Contributions & Feedback

We welcome contributions! If you'd like to contribute, feel free to fork the repository, make changes, and submit a pull request.

Feedback is always appreciated! If you encounter issues or have suggestions for new features, please open an issue or reach out to us.

## License

This project is open-source and available under the MIT License.
!
