from helpers.data import get_records
from flask import Flask, render_template

myapp = Flask(__name__)

RECORDS = get_records()
YEARS = list(range(2009, 2018))


@myapp.route("/")
def homepage():
    return render_template('homepage.html', records=RECORDS, years=YEARS)

@myapp.route("/year/<year>")
def yearpage(year):
    yearrecords = [rec for rec in RECORDS if rec['launch'][0:4] == year]

    return render_template('year.html', records=yearrecords)


if __name__ == '__main__':
    myapp.run(debug=True, use_reloader=True)
