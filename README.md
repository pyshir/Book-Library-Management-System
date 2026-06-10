# Library Management System

A simple **Python-based Library Management System** that allows users to:

* Add new books
* Delete books
* Borrow books
* Return borrowed books
* View available books

The project stores data in CSV files and uses Python's built-in file handling features.

---

## Features

### 1. Add Book

Adds a new book to the library database.

* Prevents duplicate entries.
* Saves the updated list to `books.csv`.

### 2. Delete Book

Removes an existing book from the library.

* Checks if the book exists before deletion.

### 3. Borrow Book

Allows a user to borrow an available book.

* Removes the book from the available books list.
* Records borrowing information in `borrow.csv`.
* Stores:

  * Borrow date and time
  * Username
  * Book name

### 4. Return Book

Allows a user to return a borrowed book.

* Removes the record from `borrow.csv`.
* Adds the book back to the available books list.

### 5. Show Available Books

Displays all currently available books in the library.

---

## Project Structure

```
library-management-system/
│
├── main.py
├── books.csv
├── borrow.csv
└── README.md
```

---

## CSV File Formats

### books.csv

```
Python Programming
Java Basics
Data Structures
```

### borrow.csv

```
Date,Username,Book Name
10 30 00 | Tue 2 Jun | 2026,Jahid,Python Programming
```

---

## Requirements

* Python 3.8 or higher

No external libraries are required.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/library-management-system.git
```

Navigate to the project folder:

```bash
cd library-management-system
```

Run the program:

```bash
python main.py
```

---

## Menu

When the program starts, you will see:

```
1.Add Book
2.Delete Book
3.Borrow book
4.Return borrowed book
5.Show Available books
=
```

Enter the corresponding number to perform an operation.

---

## Example

### Borrowing a Book

```
Enter your name:
= Jahid

Enter the book name
= Python Programming

Successfully registered, Please return it in time
```

### Returning a Book

```
Enter your name:
= Jahid

Enter the book name
= Python Programming

Successfully Returned
```

---

## Known Limitations

* Only one copy of each book can exist.
* Data is stored in CSV files without encryption.
* No user authentication system.
* Returning a book only checks the book name, not the borrower name.
* Program assumes `books.csv` and `borrow.csv` already exist.

---

## Future Improvements

* User authentication
* Multiple copies of books
* Search books feature
* Due date tracking
* Fine calculation system
* Object-Oriented Programming (OOP) implementation
* Database support (SQLite/MySQL)

---

## License

This project is open source and available under the MIT License.
