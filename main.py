import pandas as pd
import matplotlib
import csv 
from user_interface import *
import os

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod 
    def add_entry(cls, date, amount, category, description):
        entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer.writerow(new_entry)
        print("Entry added succesfully")


def main():
    CSV.initialize_csv()


if __name__ == "__main__":
    main()