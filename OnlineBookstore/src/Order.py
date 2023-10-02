class Order:
    """Класс заказа"""

    list_order_status = ["В пути", "Доставлен в магазин", "Получен", "Отменен"]
    """Список статусов заказа"""

    def __init__(self, id_order, id_buyer, date_of_placing_order, date_of_order_receipt, delivery_address, order_status,
                 is_paid, list_of_products):
        self.id_order = id_order
        """id заказа"""
        self.id_buyer = id_buyer
        """id покупателя"""
        self.date_of_placing_order = date_of_placing_order
        """Дата формирования заказа"""
        self.date_of_order_receipt = date_of_order_receipt
        """Дата получения заказа"""
        self.delivery_address = delivery_address
        """Адрес доставки"""
        self.order_status = order_status
        """Статус заказа"""
        self.is_paid = is_paid
        """Статус оплаты заказа"""
        self.list_of_products = list_of_products
        """Список товаров заказа"""
        self.total_cost = 0
        """Общая сумма заказа"""
        for product in self.list_of_products:
            self.total_cost += product.cost
        self.order_receipt_code = None
        """Код получения заказа"""

    def __str__(self):
        return "\n-----Order-----\n" + str(self.id_order) + "\n" + str(self.id_buyer) + "\n" + \
            str(self.date_of_placing_order) + "\n" + str(self.date_of_order_receipt) + "\n" + \
            str(self.delivery_address) + "\n" + str(self.order_status) + "\n" + str(self.is_paid) + "\n" + \
            str(self.list_of_products) + "\n" + str(self.total_cost) + "\n---------------"
