from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API keys
groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Use the API keys in your application
