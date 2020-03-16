
import math, itertools

def getSumOfProducts(gold, nifty):
    sumOfProducts = 0
    for (goldQuote, niftyQuote) in itertools.izip(gold, nifty):
        sumOfProducts += (goldQuote * niftyQuote)
    # print('Sum of products: ', sumOfProducts)
    return sumOfProducts


def calculateCorrelation(gold, nifty): 
    n = len(gold)
    sumOfProducts = getSumOfProducts(gold, nifty)
    goldSum = sum(gold)
    niftySum = sum(nifty)
    niftySquareSum = sum(list(map(lambda x: x * x, nifty)))
    goldSquareSum = sum(list(map(lambda x: x * x, gold)))

    numerator = ((n * sumOfProducts) - (niftySum * goldSum))
    denominator = (math.sqrt((n * niftySquareSum) - (niftySum * niftySum))) * (math.sqrt((n * goldSquareSum) - (goldSum * goldSum)))

    # print('Numerator and denominator: ', numerator, denominator)

    return (numerator / denominator)