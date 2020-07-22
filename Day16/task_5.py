from flask import Flask
import math

app = Flask(__name__)


@app.route('/two_pow/<int:number>')
def pow(number):
    return f'{2**number}'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
