from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        car = 0
        res0 = ListNode(0)
        res = res0
        while (l1 or l2):
            if (l1):
                l1v = l1.val
            else:
                l1v = 0
            if (l2):
                l2v = l2.val
            else:
                l2v = 0
            s = (l1v + l2v + car) % 10
            car = (l1v + l2v + car) // 10
            res.val = s
            if (l1):
                l1 = l1.next
            if(l2):    
                l2 = l2.next
            if (l1 or l2):
                res.next = ListNode(0)
                res = res.next
        if (car == 1):
            res.next = ListNode(car)
        return(res0)   
tt = ListNode(7)
num1 = ListNode(7,tt)
num2 = ListNode(9)
ans = Solution().addTwoNumbers(num1,num2)
print (ans.val,ans.next.val)     