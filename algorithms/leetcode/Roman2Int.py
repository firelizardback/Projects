class Solution:
    def romanToInt(self, s: str) -> int:
        su = 0
        options = {'I' : 1,
           'V' : 5,
           'X' : 10,
           'L' : 50,
           'C' : 100,
           'D' : 500,
           'M' : 1000}
        #print(self.romanC2Int('X'))
        for i in range(len(s)-1,-1,-1):
            if (i < len(s)-1):
                if(options[s[i]] < options[s[i+1]]):
                    sign = -1
                else:
                    sign = 1
            else:
                sign = 1
            su = su + options[s[i]]*sign
        return(su)

print (Solution().romanToInt('MCMXCIV'))