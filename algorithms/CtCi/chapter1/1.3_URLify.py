def URLify(str,trueLength):
    
    countSpace = 0
    for i in range(trueLength):
        if str[i] == ' ':
            countSpace += 1
    index = trueLength + countSpace * 2
    resStr = list(" " * index)    
    for i in range(trueLength-1,-1,-1):
        if str[i] == ' ':
            resStr[index-1] = '0'
            resStr[index-2] = '2'
            resStr[index-3] = '%'
            index -= 3
        else:
            resStr[index-1] = str[i]            
            index -= 1        
    return("".join(resStr))

print(URLify('Hello How are you?',18))