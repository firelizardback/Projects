def checkReplacement(str1,str2):
    if len(str1) != len(str2):
        return False
    oneDifference = False 
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if oneDifference:
                return False
            oneDifference = True
    return True

def checkInsert(str1,str2):
    if len(str1) != len(str2) + 1:
        return False
    index = 0
    oneShift = False
    for i in range(len(str2)):
        if str1[index] != str2[i]:
            if index != i:
                return False
            index += 1
        index += 1
    return True

def checkOneAway(str1,str2):
    
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str1) > len(str2):
        return(checkInsert(str1,str2))
    elif len(str1) < len(str2):
        return(checkInsert(str2,str1))
    else:
        return(checkReplacement(str1,str2))
        

str1 = input("String1:")
str2 = input("String2:")
print(checkOneAway(str1,str2))