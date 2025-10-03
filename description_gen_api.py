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