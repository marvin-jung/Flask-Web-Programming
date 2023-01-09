from flask import Flask
from flask.views import MethodView

app = Flask(__name__)

class UserView(MethodView):
    def get(self, user_id):
        if user_id is None:
            # return a list of users
            return 'all'
        else:
            # expose a single user
            return 'one'
        
    def post(self):
        return 'post'
    
    def put(self, user_id):
        return 'put'
    
    def delete(self, user_id):
        return 'delete'
    
user_view = UserView.as_view('users')
app.add_url_rule('/users', defaults = {'user_id' : None}, view_func = user_view, methods = ['GET'])
app.add_url_rule('/users', view_func = user_view, methods = ['POST'])
app.add_url_rule('/users/<int:user_id>', view_func = user_view, methods = ['GET', 'PUT', 'DELETE'])  

# MethodView 클래스는 get(), post(), put(), delete() 함수를 제공합니다. 
# 전체 유저 얻기와 특정 유저 얻기 기능 - /users와 /users/<int:user_id>로 나누어 같은 함수를 바라보지만 분기를 통해 서로 다르게 작동
# 유저 생성은 /users로 동일하지만 POST 메서드를 지정해 작동하도록 만듬
