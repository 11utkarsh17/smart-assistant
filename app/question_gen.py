import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}


def generate_challenge_questions(document_text):
    return """Q1. What is the main skill of the applicant?
Q2. Which frameworks has the applicant worked with?
Q3. How does the applicant contribute to team collaboration?
"""


def evaluate_answer(document_text, question, user_answer):
    if not user_answer.strip():
        return "⚠️ Please enter a valid answer to evaluate."

    return (
        f"✅ Evaluation Complete:\n\n"
        f"**Question:** {question}\n"
        f"**Your Answer:** {user_answer}\n\n"
        f"✅ This seems like a relevant answer based on the document.\n\n"
        f"*Note: This is a mock evaluation. Replace with AI later if needed.*"
    )
