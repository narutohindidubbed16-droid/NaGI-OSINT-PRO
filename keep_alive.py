from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "🟢 Nagi OSINT PRO — Bot is Alive!"

def run():
    # Render & Railway friendly port
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    thread = Thread(target=run)
    thread.start()
