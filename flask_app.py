from flask import Flask, request, json
from settings import token, confirmation_token
import messageHandler
import view

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index_page():
    return view.index_page()

@app.route('/info')
def info_page():
    return view.info_page()

@app.route('/log')
def log_page():
    return view.log_page()

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'


if __name__ == '__main__':
   app.run(debug=True, port=5000)
