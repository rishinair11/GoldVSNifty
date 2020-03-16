from gold import getGoldQuotes
from nifty import getNiftyQuotes
from correlation import calculateCorrelation
import random, sys
import matplotlib.pyplot as plt

randomizationCount = int(sys.argv[1])

gold_url = 'https://in.investing.com/commodities/gold-historical-data?end_date=1584210600&st_date=1552847400'
# Disguise request as coming from Browser
gold_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

goldQuotes = getGoldQuotes(gold_url, gold_headers)
niftyQuotes = getNiftyQuotes()

correlations = []
for i in range(0, randomizationCount):
    randomNiftyQuotes = random.sample(niftyQuotes, len(goldQuotes))
    r = calculateCorrelation(goldQuotes, randomNiftyQuotes)
    correlations.append(r)

print(correlations)

plt.plot(range(0, randomizationCount), correlations)
plt.ylabel('Pearson Coefficients')
plt.title('Gold vs Nifty correlation')
plt.show()