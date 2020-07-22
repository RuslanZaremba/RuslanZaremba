from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def date():
    return f'{datetime.today()}'


if __name__ == '__main__':
    app.run()
