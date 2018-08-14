import os
import pandas as pd
from math import isnan

def to_one_hot():
    x_train = pd.DataFrame()
    for col in x_label:
        if data[col].dtype == 'O':
            s = pd.Series(data[col])
            temp_df = pd.get_dummies(s)
            x_train = pd.concat([x_train.reset_index(drop=True), temp_df], axis=1)
        else:
            x_train = pd.concat([x_train.reset_index(drop=True), data[col]], axis=1)

    y_train = [1 if val=='야간' else 0 for val in data[y_label].values]
    y_train = pd.DataFrame(y_train)


# test  = pd.read_csv('./data/'+'test.csv', encoding='euc-kr')
train = pd.read_csv('./data/'+'train.csv', encoding='euc-kr')

# test.columns
x_label = ['당사자종별_1당_대분류', '당사자종별_2당_대분류']
y_label = '사고유형_대분류'


train[['사고유형_대분류','당사자종별_1당_대분류','당사자종별_2당_대분류']]


set(train['사고유형_대분류'])
set(train['당사자종별_1당_대분류'])
set(train['당사자종별_2당_대분류'])


train[train['사고유형_대분류']=='건널목']['당사자종별_1당_대분류']
train[train['사고유형_대분류']=='건널목']['당사자종별_2당_대분류']

