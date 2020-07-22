from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello world!'


def world():
    return 'World'


if __name__ == '__main__':
    app.add_url_rule('/hello', 'hello', hello)
    print(app.url_map)
    app.run()
