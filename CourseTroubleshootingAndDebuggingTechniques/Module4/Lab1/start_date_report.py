#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_file_data(url):
    """Downloads, processes and returns data contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    decoded_lines = [line.decode("UTF-8") for line in response.iter_lines()]

    rows = list(csv.reader(decoded_lines[1:]))
    return {f"{row[0]} {row[1]}": datetime.datetime.strptime(f"{row[3]}", '%Y-%m-%d') for row in rows}


def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)


employee_dates = get_file_data(FILE_URL)


def list_newer(start_date, end_date=datetime.datetime.today(), data=None):
    if data is None:
        data = employee_dates
    newer_list = {k: v for k, v in sorted(data.items() , key=lambda item: item[1]) if start_date <= v < end_date}
    for k in newer_list:
        print(k, newer_list.get(k).strftime('%b %d, %Y'))


def main():
    start_date = get_start_date()
    list_newer(start_date)


if __name__ == "__main__":
    main()
