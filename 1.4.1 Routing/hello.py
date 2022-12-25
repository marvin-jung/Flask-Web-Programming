from flask import Flask

app = Flask(__name__)  # Flask 객체의 인자로 __name__이 들어갑니다. 해당 인자는 정적 파일과 템플릿을 찾는데 쓰입니다.

@app.route('/index')   # route 데코레이션을 사용해 URL을 생성합니다.
@app.route('/')        # route는 중첩할 수 있습니다.
def hello_world():
    return 'Hello, World'