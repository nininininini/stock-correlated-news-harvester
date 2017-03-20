import csv
from datetime import datetime

import pandas

from utils import log_helper

date_column_header = 'Date'
price_column_header = 'Adj Close'

log = log_helper.get_logger("FileHelper")


def read_stock_history_file(file_path):
    stock_history_df = pandas.read_csv(file_path)
    stock_history_dict = dict()

    for _, row in stock_history_df.iterrows():
        stock_history_dict[datetime.strptime(row[date_column_header], "%Y-%m-%d").date()] = row[price_column_header]

    return stock_history_dict
