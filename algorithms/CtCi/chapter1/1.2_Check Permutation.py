def CheckPermutation(str1,str2):
    if len(str1) != len(str2):
        return False
    dic = dict()
    for char in str1:
        dic[char] = dic.get(char,0) + 1
    for char in str2:
        if char not in dic:
            return False
        if dic[char] == 0:
            return False
        else:
            dic[char] = dic[char] - 1
    return True   

str1 = input("String1:")
str2 = input("String1:")
print(CheckPermutation(str1,str2))

