from flask import Flask, render_template
from flask.views import View

app = Flask(__name__)

class UserList(View):
    def dispatch_request(self):
        users = []
        return render_template('users.html', users = users)

app.add_url_rule('/users', view_func = UserList.as_view('user_list'))

# View 클래스를 상속받습니다.
# View 클래스에서는 dispatch_request를 통해 API를 구현할 수 있습니다.
# app.add_url_rule을 통해 URL을 등록하고 as_view() 함수에 엔드포인트 이름을 전달해서 구현합니다.
# as_view()로 들어가는 인자를 통해 인스턴스화됩니다.