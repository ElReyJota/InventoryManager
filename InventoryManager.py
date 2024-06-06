# Imports what we need
import pandas as pd
import sqlite3 as sql
import textwrap

file = "Inventory.db"
con = sql.connect(file)
cursor = con.cursor()

def products_menu():
    """
    Manages the products menu and its options
    """
    # Initialize the Variables
    stop = False
    response = 0
    query = ""
    id = 0
    name = ""
    category = ""
    valid = False
    # Loop and processes
    while not stop:
        # Menu
        print(textwrap.dedent("""
              == Product Menu ==
              -1.Quit
              1.View Products
              2.Edit Product
              3.Add Product
              4.Delete Product"""))
        response = input_checker_int("What's your response?: ", [-1,1,2,3,4])
        valid = False
        match response:
            # Steps out of the menu
            case -1:
                stop = True
                return
            # Prints the table
            case 1:
                print(pd.read_sql_query("SELECT * FROM products;", con))
            # Process to modify a product
            case 2:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM products", con))
                    id = input_checker_int("Which product to modify?(id): ")
                    name = input("What's the new name?: ")
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    category = input("Select a category: ")
                    try:
                        query=f"UPDATE products SET name = '{name}', category = '{category}' WHERE productID = {id}"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Product succesfully modified!")
            # Process to add a product
            case 3:
                while not valid:
                    name = input("What's the name of the product?: ")
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    category = input("Select a category: ").strip()
                    try:
                        query =f"INSERT INTO products (name, category) VALUES ('{name}', '{category}');"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Product succesfully added!")
            # Process to delete a product
            case 4:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM products", con))
                    id = input_checker_int("Which product to delete?(id): ")
                    try:
                        query=f"DELETE FROM products WHERE productID='{id}'"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Product succesfully deleted!")

def categories_menu():
    """
    Manages the categories menu and its options
    """
    # Initializes variables
    stop = False
    response = 0
    query = ""
    name = ""
    category = ""
    valid = False
    # Loop and processes
    while not stop:
        # Menu
        print(textwrap.dedent("""
              == Categories Menu ==
              -1.Quit
              1.View Categories
              2.Edit Category
              3.Add Category
              4.Delete Category"""))
        response = input_checker_int("What's your response?: ", [-1,1,2,3,4])
        valid = False
        match response:
            # Quits the menu
            case -1:
                stop = True
                return
            # Prints the table
            case 1:
                print(pd.read_sql_query("SELECT * FROM categories;", con))
            # Process to modify a category
            case 2:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    name = input("Which category to modify?: ")
                    category = input("What's the new name?: ")
                    try:
                        query=f"UPDATE categories SET category = '{category}' WHERE category = '{name}'"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Category succesfully modified!")
            # Process to add a category
            case 3:
                while not valid:
                    category = input("What's the name of the category?: ")
                    try:
                        query =f"INSERT INTO categories VALUES ('{category}');"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Category succesfully added!")
            # Process to delete a category
            case 4:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    category = input("Which category to delete?: ")
                    try:
                        query=f"DELETE FROM categories WHERE category='{category}'"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Category succesfully deleted!")

def sales_menu():
    """
    Manages the sales menu and its options
    """
    # Initializes variables
    stop = False
    response = 0
    query = ""
    id = 0
    amount = 0
    valid = False
    avg = 0
    total = 0
    # Loop and processes
    while not stop:
        # Menu
        print(textwrap.dedent("""
              == Sales Menu ==
              -1.Quit
              1.View Sales
              2.Edit Sale
              3.Add Sale
              4.Delete Sale
              5.Status"""))
        response = input_checker_int("What's your response?: ", [-1,1,2,3,4,5])
        valid = False
        match response:
            # Quits the menu
            case -1:
                stop = True
                return
            # Prints the table
            case 1:
                print(pd.read_sql_query("SELECT * FROM sales;", con))
            # Process to modify a sale
            case 2:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM sales", con))
                    id = input_checker_int("Which sale to modify?(id): ")
                    amount = round(input_checker_float("What is the new amount?: "), 2)
                    try:
                        query=f"UPDATE sales SET amount = {amount} WHERE salesID = {id}"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Sale succesfully modified!")
            # Process to add a sale
            case 3:
                while not valid:
                    amount = round(input_checker_float("What's the amount of the sale?: "), 2)
                    try:
                        query =f"INSERT INTO sales (amount) VALUES ({amount});"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Sale succesfully added!")
            # Process to delete a sale
            case 4:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM sales", con))
                    id = input_checker_int("Which sale to delete?(id): ")
                    try:
                        query=f"DELETE FROM sales WHERE salesID={id}"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Sale succesfully deleted!")
            # Shows stats relevant to sales
            case 5:
                avg = pd.read_sql_query("SELECT AVG(amount) as AVG FROM sales",con)
                total = pd.read_sql_query("SELECT SUM(amount) as SUM FROM sales", con)
                print(textwrap.dedent(f"""
                        == Stats ==
                        Average Sale: {avg["AVG"][0]}
                        Total Sales: {total["SUM"][0]}
                        """))


def stocks_menu():
    """
    Manages the stocks menus and its options
    """
    # Initializes variables
    stop = False
    response = 0
    query = ""
    id = 0
    food_id = 0
    category = ""
    quantity = 0
    valid = False
    restock = 0
    # Loop and processes
    while not stop:
        # Menu
        print(textwrap.dedent("""
              == Stocks Menu ==
              -1.Quit
              1.View Stocks
              2.Edit Stock
              3.Add Stock
              4.Delete Stock
              5.Status"""))
        response = input_checker_int("What's your response?: ", [-1,1,2,3,4,5])
        valid = False
        match response:
            # Quits the menu
            case -1:
                stop = True
                return
            # Prints the table
            case 1:
                print(pd.read_sql_query("SELECT * FROM stocks;", con))
            # Process to modify a stock
            case 2:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM stocks", con))
                    id = input_checker_int("Which stock to modify?(id): ")
                    print(pd.read_sql_query("SELECT * FROM products", con))
                    food_id = input_checker_int("What is the new product?(id): ")
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    category = input("What is the new category?: ")
                    quantity = input_checker_int("What is the new quantity?: ")
                    try:
                        query=f"UPDATE stocks SET productID = {food_id}, category='{category}', quantity={quantity} WHERE stockID = {id}"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Stock succesfully modified!")
            # Process to add a stock
            case 3:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM products", con))
                    food_id = input_checker_int("What is the product?(id): ")
                    print(pd.read_sql_query("SELECT * FROM categories", con))
                    category = input("What is the category?: ")
                    quantity = input_checker_int("What is the quantity?: ")
                    try:
                        query =f"INSERT INTO stocks (productID, category, quantity) VALUES ({food_id},'{category}',{quantity});"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Stock succesfully added!")
            # Process to delete a stock
            case 4:
                while not valid:
                    print(pd.read_sql_query("SELECT * FROM stocks", con))
                    id = input_checker_int("Which stock to delete?(id): ")
                    try:
                        query=f"DELETE FROM stocks WHERE stockID={id}"
                        cursor.execute(query)
                        con.commit()
                        valid = True
                    except:
                        print("Invalid Entries")
                    print("Stock succesfully deleted!")
            # Shows relevant information about stocks
            case 5:
                restock = pd.read_sql_query("SELECT COUNT(*) as COUNT FROM stocks WHERE quantity=0;", con)
                print(f"Currently there are {restock["COUNT"][0]} stock/s that need restock.")
                print(pd.read_sql_query("SELECT * FROM stocks WHERE quantity=0;", con))

def input_checker_float(question, list=[]):
    """
    Outputs a question, gets the input and checks if its a float
    Arguments:
        Question (string): The output of the function.
        list (FloatList): If desired, acceptable answers
    Returns:
        An int from the input
    """
    # Initialize variables
    stop = False
    response = ""
    while not stop:
        response = input(question).strip()
        response
        try:
            if not list:
                return float(response)
            elif float(response) in list:
                return float(response)
            else:
                int("p")
        except:
            print("Invalid input")

def input_checker_int(question, list=[]):
    """
    Outputs a question, gets the input and checks if its an int
    Arguments:
        Question (string): The output of the function.
        list (IntList): If desired, acceptable answers
    Returns:
        An int from the input
    """
    # Initialize variables
    stop = False
    response = ""
    while not stop:
        response = input(question).strip()
        response
        try:
            if not list:
                return int(response)
            elif int(response) in list:
                return int(response)
            else:
                int("p")
        except:
            print("Invalid input")

def main():
    # Initialize variables
    menu = True
    response = 0
    print("=================================== Inventory Manager ===================================")
    while menu:
        print(textwrap.dedent("""
              == Main Menu ==
              -1.Quit 
              1.Products
              2.Categories 
              3.Sales 
              4.Stocks """))
        response = input_checker_int("What is your response?: ", [-1,1,2,3,4])
        match response:
            case -1:
                menu = False
            case 1:
                products_menu()
            case 2:
                categories_menu()
            case 3:
                sales_menu()
            case 4:
                stocks_menu()


if __name__ == "__main__":
    main()