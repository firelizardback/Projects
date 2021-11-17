class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = next

def isPalindrom(head):
    valList = []
    while(head):
        valList.append(head.val)
        head = head.next
    for i in range(len(valList)//2):
        if (valList[i] != valList[len(valList)-i-1]):
            return False
    return True


test = Node(5,Node(6,Node(9,Node(6,Node(5)))))
test2 = Node(5,Node(5))
print(isPalindrom(test2))