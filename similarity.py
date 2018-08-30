import count_similarity as cs
import pandas as pd

obj = cs.cnt_silmilarity()
obj.set_trainset('./data/train.csv', encode='utf8')

# obj.remove_columns('주야')
# obj.remove_columns('발생지시도')
# obj.remove_columns('사고유형_중분류')
# obj.remove_columns('법규위반')
# obj.remove_columns('사망자수')
# obj.remove_columns('경상자수')
# obj.remove_columns('부상신고자수')
# obj.remove_columns('중상자수')
# obj.remove_columns('사상자수')

# obj.remove_columns('요일')
obj.rulebase_typeOfAccident()
obj.rulebase_typeOfObject2()
obj.similarity()


for key in obj.similarity_cost.keys():
    index = obj.get_low_cost_index(key)
    # if len(index) >= 3:
    # if obj.similarity_mincost[key] <= 3:
    if str(obj.test.values[key][0]) == 'nan':
        print('miss value cnt : ', obj.similarity_mincost[key])
        print(obj.test.values[key])
        temp = []
        for i in index:
            temp.append(obj.train.values[i][0])
            #print(obj.train.values[i][1])
        print(pd.Series(temp).value_counts())
        print('-'*100)