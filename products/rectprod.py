from products import product

class RectProd(product.Product):
    def __init__(self, a, b, c, name):
        super(RectProd, self).__init__(a, b, c, name)

