import os
import requests
from dotenv import load_dotenv

load_dotenv()

# ✅ Using real summarization model hosted by Hugging Face
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def generate_summary(text):
    # Hugging Face API accepts limited input size (~1500 characters recommended)
    text = text.strip()
    if len(text) > 1500:
        text = text[:1500]

    payload = {"inputs": text}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        else:
            return "⚠️ Hugging Face returned an unexpected format."

    except requests.exceptions.RequestException as e:
        return f"❌ API Request Failed: {e}"

    except (ValueError, IndexError, KeyError):
        return "⚠️ Error while parsing summarization response."
