def checkIsUnique(str):
    defUniqueLength = 128
    indexTable = [False] * defUniqueLength
    if len(str) > defUniqueLength:
        return False
    for char in str:
        print(char)
        if indexTable[ord(char)]:
            return False
        indexTable[ord(char)] = True
    return True

inputStr = input("Enter string to search through for unique characters:") 
print(checkIsUnique(inputStr))