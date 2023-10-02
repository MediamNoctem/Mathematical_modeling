from User import User
from ShoppingCart import ShoppingCart
from Order import Order
from datetime import datetime


class Buyer(User):
    """Класс авторизованных покупателей"""

    def __init__(self, id_user, type_user, login, password, lastname, firstname, patronymic, birthdate):
        super().__init__(id_user, type_user, login, password, lastname, firstname, patronymic, birthdate)
        self.list_of_orders = []
        """Список заказов пользователя"""
        self.shopping_cart = ShoppingCart([])
        """Корзина покупок пользователя"""

    def __str__(self):
        return "\n-----Buyer-----\n" + str(self.id_user) + "\n" + str(self.type_user) + "\n" + str(self.login) + "\n" + \
            str(self.lastname) + "\n" + str(self.firstname) + "\n" + str(self.patronymic) + "\n" + str(self.birthdate) \
            + "\n" + str(self.list_of_orders) + "\n" + str(self.shopping_cart.__str__()) + "\n---------------"

    def make_order(self, id_order, delivery_address):
        """Сделать заказ"""
        order = Order(id_order, self.id_user, datetime.now(), None, delivery_address,
                      Order.list_order_status[0], False, self.shopping_cart.list_of_products)
        self.list_of_orders.append(order)

    def add_product_to_cart(self, product):
        """Добавить товар в корзину"""
        self.shopping_cart.add_product_to_cart(product)

    def delete_product_to_cart(self, product):
        """Удалить товар из корзины"""
        self.shopping_cart.delete_product_to_cart(product)

    def get_order_receipt_code(self, order):
        """Получить код получения заказа"""
        return order.order_receipt_code
