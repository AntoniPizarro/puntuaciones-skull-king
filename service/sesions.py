from service.db import Data_Base as db

class Sesion:

    @staticmethod
    def check_password(host, data_base, data):
        user = {
            "username" : data["username"]
        }
        password = data["password"]
        user_list = db.get_data(host, data_base, "users", user)["data"]
        if len(user_list) == 1:
            user_data = user_list[0]
            if user_data["password"] == password:
                return True

        elif not user_list:
            return True
        
        return False