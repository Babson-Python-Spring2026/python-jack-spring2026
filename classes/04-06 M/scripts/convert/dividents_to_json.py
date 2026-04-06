import csv
import json

dividends_by_date = {}
dividends_by_tic = {}

with open('classes/04-06 M/data/source/portfolio_dividends.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        date, ticker, dividend_str = row

        dividend_amount = float(dividend_str)

        dividends_by_date.setdefault(date, []).append({
            'ticker': ticker,
            'dividend': dividend_amount
        })

        dividends_by_tic.setdefault(ticker, []).append({
            'date': date,
            'dividend': dividend_amount
        })

with open('classes/04-06 M/data/system/dividends_ticker.json', 'w') as f:
    json.dump(dividends_by_tic, f, indent=2)

with open('classes/04-06 M/data/system/dividends_dates.json', 'w') as f:
    json.dump(dividends_by_date, f, indent=2)
