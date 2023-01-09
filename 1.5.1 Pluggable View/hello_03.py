class UserList(View):
    methods = ['GET', 'POST']
    
    def dispatch_request(self):
        users = []
        return render_template('users.html', users = users)
    
class UserList(MethodView):
    decorators = [user_required]
