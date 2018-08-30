import os
import pandas as pd
import numpy as np

filename = "train.csv"
data = pd.read_csv('./data/'+filename, encoding='utf-8')

merge_col = []
for a,b in data[['주야','요일']].values:
    merge_col.append(a+b)
#data = pd.concat([data,pd.DataFrame(merge_col)], axis=1)

x_label = ['사망자수', '사상자수', '중상자수', '경상자수', '부상신고자수', '발생지시도', '발생지시군구', '사고유형_대분류', '당사자종별_2당_대분류']
y_label = '법규위반' # '사고유형_중분류'
x_label = ['사고유형_대분류', '사고유형_중분류', '법규위반', '도로형태_대분류', '도로형태', '당사자종별_1당_대분류', '당사자종별_2당_대분류']
y_label = '시간'

# x_label = ['부상신고자수', '사고유형_대분류', '법규위반','당사자종별_2당_대분류']
# y_label = '도로형태_대분류' #'당사자종별_1당_대분류'

#categorical -> one hot

x_train = pd.DataFrame()
for col in x_label:
    if data[col].dtype == 'O':
        s = pd.Series(data[col])
        temp_df = pd.get_dummies(s)
        x_train = pd.concat([x_train.reset_index(drop=True), temp_df], axis=1)
    else:
        x_train = pd.concat([x_train.reset_index(drop=True), data[col]], axis=1)

# y_train = [1 if val=='야간' else 0 for val in data[y_label].values]
# y_train = pd.DataFrame(y_train)
y_train = data[y_label]


#train, test split
np.random.seed(2018)
train_index = np.random.rand(len(y_train)) < 0.8

x_test = x_train[~train_index]
y_test = y_train[~train_index]
x_train = x_train[train_index]
y_train = y_train[train_index]

#random forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=1000, oob_score= True, random_state=2018, max_features=10)
rf.fit(x_train, y_train)

#acc
from sklearn.metrics import accuracy_score
predicted = rf.predict(x_test)
accuracy = accuracy_score(y_test, predicted)
print(rf.oob_score_, accuracy)

#confusion matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.metrics import confusion_matrix
# cm = pd.DataFrame(confusion_matrix(y_test, predicted))
# sns.heatmap(cm, annot=True)
# plt.show()


# #features importances
# for name, importance in zip(x_train.columns, ):
#     print(name, "=", importance)

# indices = np.argsort(rf.feature_importances_)

