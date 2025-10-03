
 # token#        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

# import requests
#
# HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
# HUGGINGFACE_TOKEN = "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"
#
# headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
#
# def describe_mesh(mesh):
#     """Ask Hugging Face model to describe a mesh based on its stats."""
#     prompt = f"Describe a 3D model named {mesh.name} with {mesh.vertices} vertices and {mesh.faces} faces."
#     payload = {"inputs": prompt, "max_length": 50}
#
#     response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
#     if response.status_code == 200:
#         data = response.json()
#         # The model returns a list of dicts like: [{"generated_text": "..."}]
#         return data[0]["generated_text"]
#     else:
#         return f"[ERROR] API call failed: {response.status_code}"

import requests

def describe_mesh(filename):
    url = "https://api.adviceslip.com/advice"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            advice = response.json()["slip"]["advice"]
            return f"{advice}"
    except Exception:
        pass
    return "[No description available]"