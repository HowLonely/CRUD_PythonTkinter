from Entity.DTO.User import User
from Entity.DAO import UserCRUD


class Login:
    def __init__(self, frame):
        self.frame = frame
        self.user = ''

    def isEmpty(self):
        return not (len(self.frame.field_user.get()) != 0
                    and len(self.frame.field_pass.get()) != 0)

    def verifLogIn(self):
        return UserCRUD.show_one(self.frame.field_user.get()) is not None and \
               UserCRUD.show_one(self.frame.field_user.get())[3] == self.frame.field_pass.get()
