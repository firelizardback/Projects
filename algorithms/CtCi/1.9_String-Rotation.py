def stringRotation(str1,str2):
    if (len(str1) != len(str2) or len(str1) == 0):
        return False
    string = str1 + str1
    if str2 in string:
        return True
    else:
        return False

print(stringRotation('waterbottle','erbottlewat'))