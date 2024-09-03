import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMS = ["date", "amount", "category", "description"]
    FORMAT= "%d-%m-%Y"

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
            "date": datetime.strptime(date, cls.FORMAT),
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer.writerow(entry)

    @classmethod
    def get_entries(cls, start_date: str, end_date: str):
        df = pd.read_csv(cls.CSV_FILE)
        start_date_formated = datetime.strptime(start_date, cls.FORMAT)
        end_date_formated = datetime.strptime(end_date, cls.FORMAT)
        df["date"] = df["date"].apply(lambda x : datetime.strptime(x, cls.FORMAT) )
        mask = ((df["date"]>=start_date_formated) & (df["date"]<=end_date_formated))
        entries = df.loc[mask]
        return entries
    

CSV.get_entries("02-02-2002", "02-02-2025")