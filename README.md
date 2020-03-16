# **Correlation between Nifty50 and Gold**

### Calculates the correlation between one year from March 2019 to March 2020, the price quotes of the Gold and the Nifty50 indices.
Type of correlation is the Pearson Correlation Coefficient. (https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

 ## How to get it running?

- ### `pip install -r requirements.txt`
- ### Download the nifty stock quotes of the year from https://www1.nseindia.com/products/content/equities/indices/historical_index_data.htm and store it in the `nifty` folder as `nifty.csv`
- ### python main.py [randomization_count] 
##### (randomization count is the number of random permutations to run the correlation function against)