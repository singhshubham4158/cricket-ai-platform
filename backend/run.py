from app import create_app, socketio
from app.sockets import start_stream

app = create_app()

if __name__ == "__main__":
    socketio.start_background_task(start_stream)  # 🔥 MUST BE HERE
    socketio.run(app, debug=True)