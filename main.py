from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open('index.html', 'r', encoding='utf-8') as html_stream:
        return html_stream.read()


if __name__ == '__main__':
    app.run(port=800, host='127.0.0.1', debug=True)
