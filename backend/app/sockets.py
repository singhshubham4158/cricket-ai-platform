from . import socketio
from services.fetch_api import get_live_match

def start_stream():
    print("🔥 WebSocket stream started")

    while True:
        data = get_live_match()
        print("Sending data:", data)  # 👈 DEBUG

        socketio.emit("live_update", data)
        socketio.sleep(5)