import pandas as pd
import matplotlib
import csv 
from user_input import *
from csv_handling import CSV
import os

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date (dd-mm-yyyy) or press enter to add the actual date:", True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Entry added succesfully")


def view_transactions():
    startdate=get_date("Enter the start date (dd-mm-yyyy): ")
    end_date = get_date("Enter the end date (dd-mm-yyyy): ")
    csv_entries = CSV.get_entries(startdate, end_date)
    print(csv_entries)



def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3.Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
           add()

        elif choice =="2":
            view_transactions()

        elif choice =="3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()