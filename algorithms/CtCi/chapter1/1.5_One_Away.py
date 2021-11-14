def checkOneAway(str1,str2):
    
    if abs(len(str1) - len(str2)) > 1:
        return False
    dic = dict()
    for ch in str1:
        dic[ch] = dic.get(ch,0) + 1
    for ch in str2:
        dic[ch] = dic.get(ch,0) - 1
    print(dic)
    oneNegative = False
    onePositive = False
    while(dic):
        key, var = dic.popitem()
        if (var == 1):
            if onePositive:
                return False
            onePositive = True
        if (var == -1): 
            if oneNegative:
                return False
            oneNegative = True
    if (len(str1) == len(str2)):
        return ((oneNegative and onePositive) or not(oneNegative and onePositive))
    else:
        return ((oneNegative and not onePositive) or (not oneNegative and onePositive)) 
 
str1 = input("String1:")
str2 = input("String2:")
print(checkOneAway(str1,str2))