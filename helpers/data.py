from pathlib import Path
import pandas as pd
DATA_PATH = Path('static', 'data', 'records.csv')


def get_records():
    data = pd.read_csv(DATA_PATH)
    return data.to_dict('records')



def get_failures(records):
    failures = []
    for r in records:
        if r['status'] == 'failed' and r['percent_funded'] < 100 and r['usd_goal'] > 10000:
            failures.append(r)
    return failures

def get_top_failures(records, n=10):
    f = sorted(get_failures(records), key=lambda x: x['percent_funded'], reverse=True)[0:n]
    return f



