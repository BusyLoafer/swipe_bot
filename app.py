from flask import Flask, request
import requests
import json

app = Flask(__name__)

def send_message(text):
    chat_id = 606850005
    method = "sendMessage"
    token = "1640600663:AAGbaFD-gwDeNlp5jKqTJcWWVfsu9ColGfY"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        send_message("pong")
    return {"ok": True}


@app.route("/swipe", methods=["POST"])
def receive_update2():
    print(request.json)
    # qwe = json.loads(request.json)
    # print(qwe.aaa)
    # print(request.json.aaa)
    send_message(request.json)
    return {"ok": True}