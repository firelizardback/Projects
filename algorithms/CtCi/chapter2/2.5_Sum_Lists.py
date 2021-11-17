class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def sumList(num1, num2):
    carry = 0
    res = Node(0)
    start = res
    if not (num1 or num2):
        return None 
    while(num1 or num2):
        if (num1):
            val1 = num1.val
            num1 = num1.next
        else:
            val1 = 0
        if (num2):
            val2 = num2.val
            num2 = num2.next    
        else:
            val2 = 0
        res.val = (val1 + val2 + carry) % 10
        carry =  (val1 + val2 + carry) // 10
        res.next = Node(0)
        previous = res
        res = res.next
    if carry == 1:
        res.val = 1
    else:
        previous.next = None
    return start

def sumListReverse(num1, num2):
    list1 = []
    list2 = []
    resList = []
    while(num1):
        list1.append(num1.val)
        num1 = num1.next
    while(num2):
        list2.append(num2.val)
        num2 = num2.next
    carry = 0
    for i in range(max(len(list1),len(list2))-1,-1,-1):
        if i < len(list1):
            val1 = list1[i]
        else:
            val1 = 0
        if i < len(list2):
            val2 = list2[i]
        else:
            val2 = 0
        resList.append((val1 + val2 + carry) % 10)
        carry =  (val1 + val2 + carry) // 10
    if carry == 1:
        resList.append(1)
    res = Node(resList[-1])
    start = res
    for i in range(len(resList)-2,-1,-1):
        res.next = Node(resList[i])
        res = res.next
    return start



#number1 = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))
num1 = Node(6,Node(1,Node(7)))
num2 = Node(2,Node(9,Node(5)))
#test = sumList(num1,num2)
test = sumListReverse(num1,num2)
print(test.val,test.next.val,test.next.next.val)
