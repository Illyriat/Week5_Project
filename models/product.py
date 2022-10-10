class Product:

    def __init__(self, model, description, stock_count, trade_price, sale_price, id = None):
        self.model = model
        self.description = description
        self.stock_count = stock_count
        self.trade_price = trade_price
        self.sale_price = sale_price
        self.id = id