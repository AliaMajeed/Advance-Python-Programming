class Data:
     def __init__(self, product , sales):
          self.product= product
          self.sales= sales

sale = Data("Toys" , 20)
print(sale.product, sale.sales)
