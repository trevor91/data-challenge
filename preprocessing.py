import os
import pandas as pd

print(os.listdir())
print(os.listdir('./data'))
filename = "train.txt"
print(filename)
data = pd.read_csv('./data/'+filename)

y_label = ['주야', '요일', '사망자수', '사상자수', '중상자수', '경상자수', '부상신고자수', '발생지시도', '발생지시군구', '사고유형_대분류', '사고유형_중분류', '법규위반', '도로형태_대분류', '도로형태', '당사자종별_1당_대분류', '당사자종별_2당_대분류']

y_cnt = {}
for col in data.columns:
    if col in y_label:
        # if len(set(data[col])) < 100:
        y_cnt[col] = len(set(data[col]))

print(y_cnt)
