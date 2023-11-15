from bookstoreModule import BookStore
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

        price=input("enter price: ")
        while(type(price)!= type(1)):
            price=int(input("price should be in numbers: "))

        quantity=input("enter quantity: ")
        while(type(quantity)!= type(1)):
            price=int(input("quantity should be in numbers: "))

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
print("Database is now, empty,")
print("Start a new programe to add books to database.")
