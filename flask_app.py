import csv
import os
from flask import Flask, request, json
from datetime import datetime, timezone, timedelta

from settings import token, confirmation_token
from vkapi import api
import messageHandler
import view


app = Flask(__name__)


def log_request(msg: 'vk_message_obj', filename: str='chat-bot/requests.log') -> None:
    headers = ['date', 'time', 'name', 'body']
    with open(filename, 'a') as log:
        writer = csv.DictWriter(log, delimiter=';', fieldnames=headers)
        if os.stat(filename).st_size == 0:
            writer.writeheader()
        dt = datetime.fromtimestamp(msg['date'], tz=timezone(timedelta(hours=3)))
        user = api.users.get(user_id=msg['user_id'])[0]
        formed_line = {
            'date': '{:%d.%m.%Y}'.format(dt),
            'time': '{:%H:%M:%S}'.format(dt),
            'name': '{} {}'.format(user['last_name'].title(), user['first_name'].title()),
            'body': msg['body'] }
        writer.writerow(formed_line)

@app.route('/index')
@app.route('/')
def index_page() -> 'html':
    return view.index_page()

@app.route('/info')
def info_page() -> 'html':
    return view.info_page()

@app.route('/log')
def log_page() -> 'html':
    return view.log_page()

@app.route('/commands')
def commands_page() -> 'html':
    return view.commands_page()

@app.route('/', methods=['POST'])
def processing() -> str:
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        log_request(data['object'])
        messageHandler.create_answer(data['object'], token)
        return 'ok'


if __name__ == '__main__':
   app.run(debug=True, port=5000)
