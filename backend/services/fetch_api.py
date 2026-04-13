import requests

API_KEY = "YOUR_API_KEY"

def get_live_match():
    try:
        url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"
        res = requests.get(url).json()

        matches = res.get("data", [])

        for match in matches:
            if match.get("score"):
                score = match["score"][0]

                return {
                    "name": match.get("name", "Unknown Match"),
                    "score": {
                        "r": score.get("r", 0),
                        "w": score.get("w", 0)
                    }
                }

        # ❌ No live match → return empty
        return None

    except Exception as e:
        print("API Error:", e)
        return None