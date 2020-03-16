import requests, os
from bs4 import BeautifulSoup
import pandas as pd

fileExists = os.path.exists('./gold/gold.csv')

def getGoldQuotes(url, headers):
    gold_quotes = []
    if not fileExists: 
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html5lib')
        tds = soup.select('td.col-last_close.u-txt-align-end.u-down')
        
        for td in tds:
            span = td.findChild("span")
            quote = span.string.replace(",", "")
            gold_quotes.append(float(quote))

        df = pd.DataFrame({
            'Close': gold_quotes
        })
        df.to_csv('./gold/gold.csv')
    else: 
        df = pd.read_csv('./gold/gold.csv', usecols=[1])
        gold_quotes = df['Close'].tolist()

    return gold_quotes