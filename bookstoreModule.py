from bookModule import book
from user import User

class BookStore:
    book_store={}
    users={}

    @classmethod
    def add_book(cls,title, author, genre, price, quantity):
        newbook=book(title, author, genre, price, quantity)
        status=True
        for item in cls.book_store:
            if (cls.book_store[item].title==newbook.title and cls.book_store[item].author==newbook.author and cls.book_store[item].genre==newbook.genre and cls.book_store[item].price==newbook.price and cls.book_store[item].quantity==newbook.quantity):
                cls.book_store[item].add_quantity(1)
                status=False
        if(status==True):
            key=len(cls.book_store)+1
            cls.book_store[key]=newbook
            print("add_book: cls.book_store[key].title: ",cls.book_store[key].title)
        print("Given book added to database, successfully.")
        input("Return to Main Menu: (Press any key): ")

    @classmethod
    def remove_book(cls,title,author):
        status=True
        for item in cls.book_store:
            print("item: ",item, ", cls.book_store[item]: ",cls.book_store[item])
            print("cls.book_store[item].title: ",cls.book_store[item].title, "title: ", title, "author: ", author)
            if (cls.book_store[item].title==title and cls.book_store[item].author==author):
                print("inside test check.")
                cls.book_store[item].remove_quantity(1)
                print("One book removed from collection.")
                if (cls.book_store[item].quantity==0):
                    cls.book_store.pop(item)
                    print("Book no longer exits in database: ")
                else:
                    print("remaining count of this book: ",cls.book_store[item].quantity)
                status=False
            break
        if(status==True):
            print("Book does not exist in inventory")

        input("Return to Main Menu: (Press any key): ")
        

    @classmethod
    def search_by_title(cls,title): 
        list_by_title=[]
        book_list=[]
        status=True
        for item in cls.book_store:
            if (cls.book_store[item].title==title):
                list_by_title.append(cls.book_store[item])
                status=False
        if(status==True):
            print("There is no Book of this title")
        
        for item in list_by_title:
            dict={}
            dict["title"]=item.title
            dict["author"]=item.author
            dict["genre"]=item.genre
            dict["price"]=item.price
            dict["quantity"]=item.quantity

            book_list.append(dict)
        print("Books with specific title: ")
        print(book_list)
        input("Return to Main Menu: (Press any key): ")
    
    @classmethod
    def search_by_author(cls,author): 
        list_by_auth=[]
        book_list=[]
        status=True
        for item in cls.book_store:
            if(cls.book_store[item].author==author):
                list_by_auth.append(cls.book_store[item])
                status=False
        if(status==True):
            return "There is no book of this author."
        
        for item in list_by_auth:
            dict={}
            dict["title"]=item.title
            dict["author"]=item.author
            dict["genre"]=item.genre
            dict["price"]=item.price
            dict["quantity"]=item.quantity

            book_list.append(dict)
        print("books of this author are: ")
        print(book_list)
        input("Return to Main Menu: (Press any key): ")

    @classmethod
    def display_books(cls):
        book_list={}
        if(len(cls.book_store)>=0):
            count=1
            for item in cls.book_store:
                dict={}
                dict["title"]=cls.book_store[item].title
                dict["author"]=cls.book_store[item].author
                dict["genre"]=cls.book_store[item].genre
                dict["price"]=cls.book_store[item].price
                dict["quantity"]=cls.book_store[item].quantity

                book_list[count]=dict
            
            print("List of all books are: ")
            print(book_list)
        else:
            print("database is empty.")
        input("Return to Main Menu: (Press any key): ")
    
    @classmethod
    def add_user(cls,name,age,address):
        user=User(name, age, address)
        print("initial key: ",len(cls.users)+1)
        user_id=len(cls.users)+1
        cls.users[user_id]=user
        print("user Successfully added to system.")