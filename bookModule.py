class book:

    def __init__(self, title, author, genre, price, quantity):
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price
        self.quantity=int(quantity)
    
    def add_quantity(self,val):
        self.quantity+=val
    
    def remove_quantity(self,val):
        self.quantity-=val