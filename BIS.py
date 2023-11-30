#BIS: Books Inventory System
from bookstoreModule import BookStore
from user import User
status=True

while(status==True):
    print("Books Main Menu: ")
    print("***********************************************************************************")
    print("add book press(a): ")
    print("remove a book press(r):")
    print("Search a book by title press(t):")
    print("Search a book by author press(au)")
    print("Get a list of all books press(l): ")
    print("Quit press(x)")
    val=input("select any of the above choices: ")
    print("***********************************************************************************")

    if(val=="a" or val=="A"):
        title=input("enter title: ")
        while (len(title)<4):
            title=input("title should be atleast 4 charachters long: ")

        author=input("enter author name: ")
        while (len(author)<3):
            author=input("author should be atleast 3 charachters long: ")

        genre=input("enter genre: ")
        while(len(genre)<4):
            genre=input("genre should be atleast 4 charachters long: ")

        price=int(input("enter price: "))
        print("price of type: ",type(price))
        while(type(price)!= type(1)):
            price=int(input("price should be in numbers: "))

        quantity=int(input("enter quantity: "))
        while(type(quantity)!= type(1)):
            quantity=int(input("quantity should be in numbers: "))
        

        BookStore.add_book(title,author,genre,price,quantity)

    elif(val=="r" or val=="R"):
        title=input("enter title: ")
        while (len(title)<4):
            title=input("title should be atleast 4 charachters long: ")

        author=input("enter author name: ")
        while (len(author)<3):
            author=input("author should be atleast 3 charachters long: ")

        BookStore.remove_book(title,author)

    elif(val=="t" or val=="T"):
        title=input("enter title: ")
        while (len(title)<4):
            title=input("title should be atleast 4 charachters long: ")
        BookStore.search_by_title(title)
    
    elif(val=="au" or val=="AU" or val=="Au" or val=="aU"):
        author=input("enter author name: ")
        while (len(author)<3):
            author=input("author should be atleast 3 charachters long: ")
        BookStore.search_by_author(author)
    
    elif(val=="l" or val=="L"):
        BookStore.display_books()
    
    elif(val=="x" or val=="X"):
        status=False
    else:
        pass
user_menu=True
while user_menu:
    print("user Menu: ")
    print("user signup: press (s): ")
    print("user signin: press (i or I): ")

    val=input("select any of the above choices: ")
    print("***********************************************************************************")

    if(val=="S"or val=="s"):
        name=input("enter name")
        while len(name)<3:
            name=input("name should be atleast 3 charachters long.")
        age=int(input("enter age in number: "))
        while type(age)!=type(2) and age<3:
            age=input("only numbers are allowed greater than 3")

        address=input("enter address: ")
        while len(address)<10:
            address=input("add address in details, atleas 10 charachters long.")
        BookStore.add_user(name,age,address)

        
    elif(val=="i" or val=="I"):
        condition=True
        while condition:
            print("BookStore.users:",BookStore.users)
            id=int(input("Please enter the id."))
            while  id not in BookStore.users:
                id=input("please enter the valid id.")

            name=input("please enter the name: ")
            while name!=BookStore.users[id].name:
                name=input("enter valid name: ")

            # password=input("please enter password: ")
            # count=0
            # while password!=BookStore.users[id].password and count<3:
            #     password=input("please enter valid password")
            #     count+=1
            # if count>=3:
            #     print("you have entered password many times, try again later.")
            #     input("press any key to return to signin again")
            #     continue

            print(f"welcome {BookStore.users[id].name}")
            print("Do you want to borrow some books. Yes(y), No(n)")
            pressed_key=input("select (y) or (n): ")
            if (pressed_key=="y" or pressed_key=="Y"):
                #sdfasd
                print("list of available books press (l) or (L):")
                status=input("press (l) or (L): ")
                # while status!="l"or status!="L":
                #     status=input("press (l) or (L): ")
                if(status=="l" or status=="L"):
                    BookStore.display_books()
                    book_id=int(input("select any book id to add to cart: "))
                    while book_id not in BookStore.book_store:
                        book_id=input("Please enter valid book_id: ")
                    if(book_id in BookStore.book_store):
                        BookStore.users[id].bookadder(book_id)
                        BookStore.users[id].display_user()

            elif (pressed_key=="n" or pressed_key=="N"):
                print("Signin Menu press (y): ")
                print("Back to Main Menu press (n):")
                decision=input("enter value (y) or (n): ")
                if decision=="y" or decision=="Y":
                    continue
                elif decision=="n" or decision=="N":
                    condition=False
    print("back to books Main Menu press (y): ")
    print("signup or signin agian press (n): ")
    backto_main_book_menu=input("select (y) or (n)")
    if(backto_main_book_menu=="y" or backto_main_book_menu=="Y"):
        user_menu=False
    elif(backto_main_book_menu=="n" or backto_main_book_menu=="N"):
        continue

print("Database is now, empty,")
print("Start a new programe to add books to database.")
