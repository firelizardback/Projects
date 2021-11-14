def CheckPalindromePermutation(str):
    carry = len(str) % 2
    dic = dict()
    for char in str:
        dic[char] = dic.get(char,0) + 1
    
    while(dic):
        key, val = dic.popitem()
        if val % 2 == 1:
            if carry != 1:
                return False
            carry = 0            
    return True 


str = input("String:")
print(CheckPalindromePermutation(str))