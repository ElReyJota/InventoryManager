# Overview

This Inventory Manager project was used for me to gain more knowledge in the use of relational databases and how they can work alongside a programming language, in this case python. This project runs completely in python and uses sql querys through pandas and sqlite3 to connect to the Inventory.db database. The software application allows you to modify, add, delete and retrieve data from the database and also has some statistics regarding the stocks and sales tables.

[InventoryManager Demo](https://youtu.be/aGrmGTdGis4)

# Relational Database

I'm using a database I created myself called "Inventory.db", it contains four tables and it connects simply between each other.

|products table      |Contains the different products to be sold            |
|--------------------|------------------------------------------------------|
|ProductID (INT)     |The code connected to each product                    |
|name (TEXT)         |The name of each product                              |
|category            |The category of each product (From categories table)  |

|categories table    |Contains the different categories to apply            |
|--------------------|------------------------------------------------------|
|Category (TEXT)     |The name and also identifier of the category          |


|sales table         |Contains the sales that were made                     |
|--------------------|------------------------------------------------------|
|salesID (INT)       |The code connected to each sale                       |
|amount (NUMERIC)    |The amount the sale was finalized for                 |

|stocks table        |Contains the stocks in the store                      |
|--------------------|------------------------------------------------------|
|stockID (INT)       |The code connected to each stock                      |
|ProductID (INT)     |The code connected to each product of each stock (products table)      |
|category (TEXT)     |The category in which the stock falls into (categories table)      |
|quantity (INT)      |The quantity of produce in the stock                  |


# Development Environment

- SqLiteStudio 3.4.4
- Visual Studio Code 1.89
- Python 3.12.3
- Pandas (Python Library)
- sqlite3 (Python Library)
- textwrap (Python Library)

# Useful Websites

- [Tutorialspoint SQL Tutorial](https://www.w3schools.com/sql/default.asp)
- [Python Sqlite Tutorial](https://pynative.com/python-sqlite/)

# Future Work

- Add user interface
- Limit sales amount and its average to have 2 decimals
- Add more statistics to the status option in sales