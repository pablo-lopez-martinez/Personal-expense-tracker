from datetime import datetime

CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date():
    date = input("Enter the date (dd-mm-yyyy) or press enter to add the actual date:")
    if date=="":
        date = datetime.now().strftime("%d-%m-%Y")
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid date")
        return get_date()
    return date

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount<0:
            raise ValueError("Error: The number hast to be less than 0")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category not in CATEGORIES:
         print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
         return get_category()
    return CATEGORIES[category]
        


def get_description():
    return input("Enter a description (optional): ")
 


get_date()