import pandas as pd
import numpy as np

class cnt_silmilarity:
    def __init__(self):
        self.test = None
        self.train = None
        self.columns = []
        self.similarity_index = {}
        self.similarity_cost = {}
        self.similarity_mincost = []

    def set_testset(self, path, encode='euc-kr'):
        print('read_test...')
        self.test = pd.read_csv(path, encoding=encode)
        return None

    def set_trainset(self, path, encode='euc-kr'):
        if self.test == None:
            self.set_testset(path.replace('train','test'))
        print('read_train...')
        self.train = pd.read_csv(path, encoding=encode)
        self.train = self.train[self.test.columns]
        return None


    def other_values_index(self, test_row, train_row):
        # val_index = [i for i, val in enumerate(test_row) if str(val)!='nan']
        # test_row = test_row[val_index]
        # train_row = train_row[val_index]
        is_same = test_row == train_row
        false_index = [i for i, val in enumerate(is_same) if val==False]
        return false_index
    
    def similarity(self):
        print('similarity()...')
        for i, test_row in enumerate(self.test.values):
            self.similarity_cost[i] = []
            self.similarity_index[i] = []
            for train_row in self.train.values:
                temp_index = self.other_values_index(test_row, train_row)
                self.similarity_index[i].append(temp_index)
                self.similarity_cost[i].append(len(temp_index))
            self.similarity_mincost.append(min(self.similarity_cost[i]))
        return None
    
    def get_low_cost_index(self, key):
        if len(self.similarity_mincost)==0:
            self.similarity()

        min_val = self.similarity_mincost[key]
        min_index = [i for i, row in enumerate(self.similarity_index[key]) if min_val==len(row)]
        return min_index
    