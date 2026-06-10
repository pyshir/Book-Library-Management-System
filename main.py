import datetime

books = []
borrow_book = {}

current_time = datetime.datetime.now()
time_format = current_time.strftime("%H %M %S | %a %w %b | %Y")

def load_book():
    with open('books.csv', 'r') as w:
        for x in w:
            x = str(x)
            x = x.replace('\n', '')
            books.append(x)

def add_book(w):
    books.insert(0, w)

def save_book():
    with open('books.csv', 'w') as w:
        for x in books:
            w.write(f'{x}\n')

def load_borrow_book():
    with open('borrow.csv', 'r') as w:
        next(w)
        for x in w:
            x = x.strip().split(',')
            borrow_book[x[0]] = x[1:]

def save_borrow_book():
    with open('borrow.csv', 'w') as w:
        w.write(f'Date,Username,Book Name\n')
        for x,y in borrow_book.items():
            w.write(f'{x},')
            counts = 0
            for z in y:
                if counts < 1:
                    w.write(f'{z},')
                    counts += 1
                else:
                    w.write(f'{z}\n')



if __name__ == '__main__':

    operation = input('1.Add Book\n2.Delete Book\n3.Borrow book\n4.Return borrowed book\n5.Show Available books\n = ')

    if operation == '1':
        # Adding New Book, Won't add if already exist
        load_book()
        new_book = input('Enter new book name\n = ')
        if new_book in books:
            print(f'Book Already exist')
        else:
            add_book(new_book)
            save_book()
            print('Book added successfully!')

    elif operation == '2':
        # Remove Book, Show Error if not in the list
        load_book()
        book_name = input('Enter The book name\n = ')
        if book_name in books:
            books.remove(book_name)
            save_book()
            print('Book has been removed Successfully!')
        else:
            print('This book is not in the list')

    elif operation == '3':
        # Borrowing books, if available
        load_book()
        load_borrow_book()
        your_name = input('Enter your name:\n = ')
        book_name = input('Enter the book name\n = ')
        if book_name in books:
            books.remove(book_name)
            save_book()
            dt = time_format
            borrow_book[dt] = [your_name,book_name]
            save_borrow_book()
            print('Successfully registered, Please return it in time')
        else:
            print('Sorry Currently book is not available!')

    elif operation == '4':
        # Returned borrowed book
        load_book()
        load_borrow_book()
        your_name = input('Enter your name:\n = ')
        book_name = input('Enter the book name\n = ')

        delete_book = None
        for i,j in borrow_book.items():
            for k in j:
                if k == book_name:
                    delete_book = i
                    break

        if delete_book is not None:
            del borrow_book[delete_book]
            books.append(book_name)
            save_book()
            save_borrow_book()
            print('Successfully Returned')
        else:
            print('Book not found on borrowed database!')

    elif operation == '5':
        load_book()
        print(books)




