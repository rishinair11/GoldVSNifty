import pandas as pd

def getNiftyQuotes():
    df = pd.read_csv('./nifty/nifty.csv', usecols=[4])
    niftyQuotes = df['Close'].tolist()
    # Convert string to float
    return list(map(lambda x: float(x) , niftyQuotes)) 


