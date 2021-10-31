from typing import List
import matplotlib.pyplot as plt
from math import log10

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if (n==1):
            return(['()'])
        out3 = set()
        for j in range(1,n//2+1):
            out = self.generateParenthesis(j)
            out2 = self.generateParenthesis(n-j)
            for k in out:
                for l in out2:
                    out3.add(k+l)
                    out3.add(l+k)
                    if (j==1):
                        out3.add('(' + l + ')')
                
        return list(out3)

x = []
y = []
for i in range(1,14):
    ans = Solution().generateParenthesis(i)
    y.append(log10(len(ans)))
    x.append(i)
    print ('Number of combination for %d is %d' % (i, len(ans)))

plt.plot(x, y)
plt.xlabel('Number of parenthesis pairs')
plt.ylabel('Log10(Number of Combination)')
plt.show()