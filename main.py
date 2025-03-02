import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE = 'fin_data.csv'

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Date', 'Amount' , 'Category' , 'Description'])
            df.to_csv(cls.CSV_FILE, index=False)

CSV.initialize_csv()