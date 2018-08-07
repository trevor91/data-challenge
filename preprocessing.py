import os
import pandas as pd
from math import isnan

test  = pd.read_csv('./data/'+'test.csv', encoding='euc-kr')
train = pd.read_csv('./data/'+'train.csv', encoding='euc-kr')
train = train[test.columns]

def comp(test, train):
    t = (test==train)
    if len(t[t==False]) == 3:
        for row in test[t==False]:
            if not str(row)=='nan':
                return False
        else:
            return True
    return False



for test_row in test.values:
    print(test_row)
    for train_row in train.values:
        if comp(test_row, train_row):
            print('\t', train_row)
