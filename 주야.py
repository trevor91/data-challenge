import os
import pandas as pd
import numpy as np

filename = "train.txt"
data = pd.read_csv('./data/'+filename, encoding='euc-kr')

# for day in list(set(data['요일'].values)):
#     temp = data[data['요일']==day]['주야'].value_counts()
#     print(day)
#     print(temp / sum(temp))


x_label = ['경상자수', '부상신고자수', '발생지시도', '발생지시군구', '사고유형_대분류', '사고유형_중분류', '법규위반', '도로형태_대분류', '당사자종별_2당_대분류']
x_label = ['발생년','요일', '사망자수', '사상자수', '중상자수', '경상자수','부상신고자수', '발생지시도', '발생지시군구', '사고유형_대분류', '사고유형_중분류', '사고유형', '법규위반_대분류','법규위반', '도로형태_대분류', '도로형태', '당사자종별_1당_대분류', '당사자종별_2당_대분류']
x_label = ['요일', '사망자수', '사상자수', '중상자수', '경상자수', '부상신고자수', '발생지시도', '발생지시군구', '사고유형_대분류', '사고유형_중분류', '법규위반', '도로형태_대분류', '도로형태', '당사자종별_1당_대분류', '당사자종별_2당_대분류']
y_label = '주야'

data['요일'] = [1 if val=='월' or val=='토' or val=='일' else 0 for val in data['요일']]

#counter
# from collections import Counter
# for col in x_label:
#     freq = Counter(data[col])
#     print(col, freq, '\n')

# for col in x_label:
#     print(data[col].value_counts(), '\n')


#categorical -> one hot
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


#train, test split
np.random.seed(2018)
train_index = np.random.rand(len(y_train)) < 0.8

x_test = x_train[~train_index]
y_test = y_train[~train_index]
x_train = x_train[train_index]
y_train = y_train[train_index]


# str -> number
# from sklearn.feature_extraction.text import CountVectorizer
# vec = CountVectorizer()
# train = vec.fit_transform(data[x_label])


#random forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=1000, oob_score= True, random_state=2018, max_features=20)
rf.fit(x_train, y_train)

#acc
from sklearn.metrics import accuracy_score
predicted = rf.predict(x_test)
accuracy = accuracy_score(y_test, predicted)
print(rf.oob_score_, accuracy)

#confusion matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = pd.DataFrame(confusion_matrix(y_test, predicted))
sns.heatmap(cm, annot=True)
plt.show()


#features importances
for name, importance in zip(x_train.columns, ):
    print(name, "=", importance)

indices = np.argsort(rf.feature_importances_)

