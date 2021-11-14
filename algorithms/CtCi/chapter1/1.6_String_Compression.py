def stringCompression(text):
    if (len(text) == 0):
        return ""
    resList = []
    indexBegin = 0
    repChar = text[0]
    for i in range(1,len(text)):
        if text[i] != repChar:
            resList.append(repChar + str(i-indexBegin))
            repChar = text[i] 
            indexBegin = i
    resList.append(repChar + str(i-indexBegin+1))
    res = "".join(resList)
    if (len(res) < len(text)):
        return res
    else:
        return text

print(stringCompression("aabcccccaaa"))
print(stringCompression("aabbccddd"))