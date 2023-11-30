class User:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.books_borrowed=[]

    def bookadder(self,newbook):
        self.books_borrowed.append(newbook)
        print("book successfully added.")
        input("Press any key to continue.")
    
    def display_user(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("address: ",self.address)
        print("books_borrowed: ",self.books_borrowed)
        