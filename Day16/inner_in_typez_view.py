from flask import Flask

app = Flask(__name__)


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'Blog Number {postID}'


@app.route('/revision/<float:revNO>')
def revision(revNO):
    return f'Revision Number {revNO}'


@app.route('/path_to/<path:myPath>')
def my_path(myPath):
    return f'My path {myPath}'

if __name__=='__main__':
    app.run()