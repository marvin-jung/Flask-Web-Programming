from flask import Flask

app = Flask(__name__)  # Flask 객체의 인자로 __name__이 들어갑니다. 해당 인자는 정적 파일과 템플릿을 찾는데 쓰입니다.

@app.route('/users/<username>') 
def get_user(username):
    return username

@app.route('/posts/<int:post_id>')        # route는 중첩할 수 있습니다.
def get_post(post_id):
    return str(post_id)

@app.route('/uuid/<uuid:uuid>')
def get_uuid(uuid):
    return str(uuid)