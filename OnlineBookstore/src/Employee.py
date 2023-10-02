from User import User


class Employee(User):
    """Класс сотрудника онлайн магазина"""

    def __init__(self, id_user, type_user, login, password, lastname, firstname, patronymic, birthdate):
        super().__init__(id_user, type_user, login, password, lastname, firstname, patronymic, birthdate)
        self.list_employee_rights = None
