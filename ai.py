import os
import requests

LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

def ask_ai(prompt):

    headers = {
        "Authorization": f"Bearer {LLAMA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(
        "YOUR_LLAMA_ENDPOINT",
        json=payload,
        headers=headers,
        timeout=60
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]