import os
import pandas as pd

#draw
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

os.listdir()

train = pd.read_csv('train.csv', encoding='euc-kr')
test = pd.read_csv('test.csv', encoding='euc-kr')

train.columns[1]
train[train[train.columns[0]] == 2017]

for year in range(2012,2018):
    print(year, ": ", train[train[train.columns[0]] == year].shape)

train.columns
test.columns

train = train[['발생년','발생년월일시']+list(test.columns)]
train.columns

for year in range(2012, 2018):
    train[train['발생년'] == year]['주야'].value_counts()


#font
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18).get_name()
plt.rc('font', family = fontprop)

#drawing
sns.pairplot(train[train['주야']=='야간'], hue = '주야')
sns.pairplot(train[train['주야']=='주간'], hue = '주야')
plt.show()