import products.rectprod as rectprod

class HotPop(rectprod.RectProd):
    '''
    16x10.7x6.2
    '''

    def __init__(self):
        super(HotPop, self).__init__(16, 10.7, 6.2, 'HotPop')

        conf1 = [self.a, self.b, self.c]
        conf2 = [self.b, self.a, self.c]
        conf3 = [self.c, self.a, self.b]
        self.configs = [conf1, conf2, conf3]

        min_pnts_a = 12
        max_pnts_a = 20
        min_pnts_b = 18
        max_pnts_b = 28
        min_pnts_c = 24
        max_pnts_c = 38

        self.analyze_dict = {self.a:[min_pnts_a, max_pnts_a], self.b:[min_pnts_b, max_pnts_b], self.c:[min_pnts_c, max_pnts_c]}


    def get_allowed_range(self, product_height):
        for conf in self.configs:
            if product_height == conf[0]:
                return self.get_min_max_allowed_pnts(product_height)

    def get_min_max_allowed_pnts(self, height):
        return self.analyze_dict[height]


