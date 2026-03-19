import requests
import os
from dotenv import load_dotenv

load_dotenv()

MURF_API_KEY = os.getenv("MURF_API_KEY")

def murf_speak(text, voice_id="en-IN-aarav"):
    """
    Generates a Murf AI voice URL for the given text.
    Best for Hackathon: en-IN-aarav (Conversational)
    """
    url = "https://api.murf.ai/v1/speech/generate"

    payload = {
        "text": text,
        "voiceId": voice_id,
        "style": "conversational",
        "format": "mp3",
        "rate": 0,
        "pitch": 0
    }

    headers = {
        "api-key": MURF_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            audio_url = response.json().get("audioFile")
            print(f"✅ Murf Success: {audio_url}")
            return audio_url
        else:
            print(f"❌ Murf Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

if __name__ == "__main__":
    # Test script
    test_text = "Welcome to Union Bank of India. How can I assist you today?"
    murf_speak(test_text)
