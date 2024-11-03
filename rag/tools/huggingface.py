import os
from langchain_community.llms import HuggingFaceHub
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Initialize the LLM
llm = HuggingFaceHub(repo_id="gpt2")  # Replace with your desired model

# Use the LLM
prompt = "What is the capital of France?"
response = llm(prompt)
print(response)

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name = "gemini-pro")
prompt_parts = [
    "Write a Python function and explain it to me",
]

response = model.generate_content(prompt_parts)
print(response.text)