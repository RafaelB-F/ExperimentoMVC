from flask import Flask, request, render_template
from controller import UserController

app = Flask(__name__)
user_controller = UserController()

@app.route('/')
def index():
    users = user_controller.get_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    user_controller.add_user(name)
    return index()

if __name__ == '__main__':
    app.run(debug=True)