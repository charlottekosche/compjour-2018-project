from pathlib import Path
import pandas as pd
DATA_PATH = Path('static', 'data', 'records.csv')


def get_records():
    data = pd.read_csv(DATA_PATH)
    return data.to_dict('records')

def get_top_10(records):
    return []
