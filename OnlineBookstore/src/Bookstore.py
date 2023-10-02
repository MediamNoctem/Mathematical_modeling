import yaml
from User import User
from Buyer import Buyer
import datetime


def save_to_yaml(obj, path_to_file):
    """Сохранить объект в файл YAML"""
    with open(path_to_file, 'a') as f:
        yaml.dump(obj, f, default_flow_style=False, explicit_start=True)


def does_user_exist(login, password):
    with open("yaml/users.yaml", "r") as f:
        for user in yaml.load_all(f, Loader=yaml.Loader):
            if user.login == login and user.password == password:
                return True
    return False


def greeting():
    print("\n\n---------------------------------------------------------\n")
    print("    Добро пожаловать к нам в книжный онлайн магазин!")
    print("    Здесь вы найдете книги на любой вкус.\n")
    print("    Сначала нужно войти в систему.")
    print("    Введите логин:")
    login = input("    ---> ")
    print("    Введите пароль:")
    password = input("    ---> ")
    if does_user_exist(login, password):
        print("\n    Вы вошли в свой аккаунт.")
    else:
        print("\n    Такого аккаунта нет в системе.")
        print("    Заполните поля, чтобы создать аккаунт.")
        print("\n---------------------------------------------------------\n")


# admin = User(0, User.list_type_user[0], "admin", "admin", "Семенов", "Марк", "Михайлович", datetime.date(1980, 1, 1))
# buyer1 = Buyer(1, User.list_type_user[3], "buyer1", "05072001", "Ромашкина", "Анастасия", "Александровна",
#                datetime.date(2001, 7, 5))
#
# save_to_yaml(admin, "yaml/users.yaml")
# save_to_yaml(buyer1, "yaml/users.yaml")

# with open("yaml/users.yaml", "r") as f:
#     for d in yaml.load_all(f, Loader=yaml.Loader):
#         print(d.id_user)

if __name__ == "__main__":
    greeting()
