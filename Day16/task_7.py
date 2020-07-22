from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/form',methods=['POST'])
def login():
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    midname = request.form['middle_name']
    age = request.form['age']
    with open('data.txt','w') as f:
        f.writelines(f'{firstname} {lastname} {midname} {age}')
    return "success"



if __name__ == '__main__':
    app.run(port=8181, debug=True)
