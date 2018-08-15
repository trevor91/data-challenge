class rulebase:
    def __init__(self):
        pass
    
    def target_typeOfAccident(self, object2):
        '''
        x : 당사자종별_2당_대분류
        y : 사고유형_대분류
        '''
        if str(object2) == 'nan': return float('nan')
        elif object2 == '보행자': return '차대사람'
        elif object2 == '열차': return '건널목'
        elif object2 == '없음': return '차량단독'
        return '차대차'
    
    def target_typeOfObject2(self, accident):
        '''
        x : 사고유형_대분류
        y : 당사자종별_2당_대분류 (자동차 종류는 맞출수없음)
        '''
        if str(accident) == 'nan': return float('nan')
        elif accident == '차대사람': return '보행자'
        elif accident == '건널목': return '열차'
        elif accident == '차량단독': return '없음'
        else: return float('nan')    
        
