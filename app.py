import re
from flask import Flask
import json
app = Flask(__name__)

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('bc2a542e8b2da619bb4a1990e82a2da8')
handler = WebhookHandler('D9O4MOGaJs+tnIBDMf3gRa1lYmXq1U/uGZFn2FsTRiSmYWxNjtmsILvg8M0YSXw9nKeJFLRv4T7+WeMfvuYQJ5xl62YzBQChvAASyHqzfujTPxad/M6awPeulkdfMIqH4SrWS+80ycpx4JR6ZlzxcwdB04t89/1O/w1cDnyilFU=')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    command = event.message.text
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="hello"))

@app.route('/send', methods=['GET'])
def send_data():
    line_bot_api.broadcast(TextSendMessage(text='?'), notification_disabled=False, timeout=None)

if __name__=='__main__':
    app.run()