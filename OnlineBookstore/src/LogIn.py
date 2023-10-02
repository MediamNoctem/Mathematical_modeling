import yaml


class LogIn:
    """Класс для регистрации и авторизации"""

    def does_user_exist(self, login, password):
        with open("yaml/users.yaml", "r") as f:
            for user in yaml.load_all(f, Loader=yaml.Loader):
                if user.login == login and user.password == password:
                    return True
        return False
