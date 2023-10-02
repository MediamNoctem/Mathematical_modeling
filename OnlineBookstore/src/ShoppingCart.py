class ShoppingCart:
    """Класс корзины пользователя"""

    def __init__(self, list_of_products):
        self.list_of_products = list_of_products
        """Список товаров, выбранных для покупки"""

    def __str__(self):
        string_list_of_products = "\n-----ShoppingCart-----"
        for product in self.list_of_products:
            string_list_of_products += product.__str__()
        string_list_of_products += "\n----------------------"
        return string_list_of_products

    def add_product_to_cart(self, product):
        """Добавить товар в корзину"""
        self.list_of_products.append(product)

    def delete_product_to_cart(self, product):
        """Удалить товар из корзины"""
        self.list_of_products.remove(product)
