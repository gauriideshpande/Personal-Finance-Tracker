import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    CSV_FILE = 'fin_data.csv'
    COLUMNS = ['Date', 'Amount', 'Category', 'Description']

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def data_entry(cls, Date, Amount, Category, Description):
        new_entry = {'Date': Date, 
                     'Amount': Amount, 
                     'Category': Category, 
                     'Description': Description,
                     }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('Data entry successful!')

# CSV.initialize_csv()
# CSV.data_entry('03-03-2025', 483, 'Food', 'Irani Cafe')

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.data_entry(date, amount, category, description)

add()