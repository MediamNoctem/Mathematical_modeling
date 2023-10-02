class User(object):
    """Общий класс пользователей книжного магазина"""

    list_type_user = ["Администратор", "Контент-менеджер", "Оператор пункта выдачи заказов", "Покупатель"]

    def __init__(self, id_user, type_user, login, password, lastname, firstname, patronymic, birthdate):
        self.id_user = id_user
        """id авторизованного пользователя"""
        self.type_user = type_user
        """Тип пользователя: покупатель или сотрудник"""
        self.login = login
        """Логин пользователя"""
        self.password = password
        """Пароль пользователя"""
        self.lastname = lastname
        """Фамилия пользователя"""
        self.firstname = firstname
        """Имя пользователя"""
        self.patronymic = patronymic
        """Отчество пользователя"""
        self.birthdate = birthdate
        """Дата рождения пользователя"""
