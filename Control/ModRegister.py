from Entity.DAO import UserCRUD
from Entity.DTO.User import User


class Register:
    def __init__(self, frame):
        self.frame = frame

    def userExist(self):
        return UserCRUD.show_one(self.frame.user.get()) is not None

    def register(self):
        if not self.frame.objReg.userExist():
            username = self.frame.user.get()
            email = self.frame.email.get()
            password = self.frame.password.get()

            u = User(username, email, password)
            UserCRUD.insert(u)
            return True
        else:
            return False
