import count_similarity as cs

obj = cs.cnt_silmilarity()
obj.set_trainset('./data/train.csv', encode='utf8')
obj.rulebase_typeOfAccident()
obj.rulebase_typeOfObject2()
obj.similarity()


for key in obj.similarity_cost.keys():
    index = obj.get_low_cost_index(key)
    if obj.similarity_mincost[key] <= 3:
        print('miss value cnt : ', obj.similarity_mincost[key])
        print(obj.test.values[key])
        for i in index:
            print(obj.train.values[i])
        print('-'*100)