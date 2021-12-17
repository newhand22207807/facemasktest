# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('yp/WcXmf2doOSJBJ7B8VlI3IL5oZuA/l13lvnJieqnFzpvazy+irc83+LufYPH8BaoK3mUANBEdmtURRP3WsZfO5DPS+5lIi/Yc3uH8dZMLOMD7YfUT5q/XR72lY0Bas5J/UQ11BwNamL5ERxgWuzQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5a09fbf475da68f637f4c1e068242849')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()