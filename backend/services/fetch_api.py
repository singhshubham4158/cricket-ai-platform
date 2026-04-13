import requests

API_KEY = "YOUR_API_KEY"

def get_live_match():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}"
    res = requests.get(url).json()

    if not res.get("data"):
        return {"error": "No live match"}

    match = res["data"][0]

    return {
        "name": match["name"],
        "score": match["score"][0]
    }