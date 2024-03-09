from model import UserModel

class UserController:
    def __init__(self):
        self.user_model = UserModel()

    def add_user(self, name):
        self.user_model.add_user(name)

    def get_users(self):
        return self.user_model.get_users()