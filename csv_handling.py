import pandas as pd
import csv

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMS = ["date", "amount", "category", "description"]
    FORMAT= "%d-%m-%y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod 
    def add_entry(cls, date: str, amount:int, category: str, description: str):
        entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer.writerow(entry)
        print("Entry added succesfully")

    @classmethod
    def get_entries(cls, start_date: str, end_date: str):
        df = pd.read_csv(cls.CSV_FILE)
        filtered = ((df["date"]>start_date) & (df["date"]<end_date))
        entries = df.loc[filtered]
        return entries