from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Gm61Rn9w148ID5PKvigKqQ6XoVsR1/gGGJpAqvg/OtaAU88ob2An4qCYO+Px4M86LYcV8BrPU0Rxxir8bpU/+2clYTM7OVLMRNlvplKGv+qBhxispafy6mKazHqiMnEkNX1ITTQDBTPT0Yjt3zsjnAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d9276ba2c28a9cdcf62f1d46a27e5b01')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()