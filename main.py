import pandas as pd
import matplotlib
import csv 
from user_input import *
from csv_handling import CSV
import os

def main():
    CSV.initialize_csv()
    CSV.add_entry("12-02-2024", 3000, "Expense", "Supermarket")
    CSV.add_entry("13-02-2024", 3000, "Expense", "Supermarket")
    CSV.add_entry("14-02-2024", 3000, "Expense", "Supermarket")
    CSV.add_entry("15-02-2024", 3000, "Expense", "Supermarket")
    CSV.add_entry("16-02-2024", 3000, "Expense", "Supermarket")
    print(CSV.get_entries("13-02-2024", "15-02-2024"))


if __name__ == "__main__":
    main()