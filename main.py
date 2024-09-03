import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    #start_date=get_date("Enter the start date (dd-mm-yyyy): ")
    #end_date = get_date("Enter the end date (dd-mm-yyyy): ")
    start_date= "02-02-2002"
    end_date= "02-02-2025"
    entries = CSV.get_entries(start_date, end_date)
    income = entries.loc[entries["category"]=="Income"]
    expense = entries.loc[entries["category"]=="Expense"]
    total_income = income["amount"].sum()
    total_expense = expense["amount"].sum()
    net_savings = total_income-total_expense
    print(entries.to_string(index=False))
    print("Summary:")
    print(f"Total income: ${total_income: .2f}")
    print(f"Total expense: ${total_expense: .2f}")
    print(f"Net savings: ${net_savings: .2f}")
    if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(entries)


def plot_transactions(df):
    df.set_index("date", inplace=True)

    income_df = (
        df[df["category"]=="Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(12,7))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()
    


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