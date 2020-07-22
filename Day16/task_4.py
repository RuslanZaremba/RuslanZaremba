from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def date():
    date = datetime.strftime(datetime.today(), "%Y/%m/%d")
    return f'{date}'


if __name__ == '__main__':
    app.run(debug=True, port=8001)
