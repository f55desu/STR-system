def avg(rateList):
    rating = 0.0
    for rate in rateList:
        rating += rateList[rate]  
    return round(rating/(float)(len(rateList)), 2)