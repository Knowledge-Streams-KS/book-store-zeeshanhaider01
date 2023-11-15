class User:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.books_borrowed=[]

    def bookadder(self,newbook):
        self.books_borrowed.append(newbook)