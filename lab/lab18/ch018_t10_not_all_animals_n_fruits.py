class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""

    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product: str, price: float):
        """Add product to the cart."""
        if product not in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product: str):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")
