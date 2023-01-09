from flask import Flask, redirect, url_for, abort

app = Flask(__name__)

@app.errorhandler(403)
def permission_denied(error):
    return '403', 403

@app.route('/')
def index():
    return redirect(url_for('user_list'))

# url_for는 함수 이름을 넣으면 해당 라우팅 URL을 반환합니다. user_list를 요청했고 /users를 반환합니다.
# redirect는 반환 받은 주소로 다시 http 요청을 합니다.

@app.route('/users')
def user_list():
    abort(403)

# user_list API가 redirect 요청을 받았고 abort() 함수로 403 에러를 발생했습니다.
# @app.errorhandler를 사용하면 403 error exception를 받아 처리할 수 있습니다.
# 403 상태 코드를 리턴합니다. 이 부분은 403 문자열을 리턴했지만 json으로 리턴하는 등 커스텀이 가능합니다.
