class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
"""
def deleteNode(head,val):
    node = head
    if node.val == val:
        return head.next
    while node.next:
        if node.next.val == val:
            node.next = node.next.next
            return head
        node = node.next
    return head


def removeDups(head):
    valSet = set()
    dupSet = set()
    node = head
    while(node):
        if node.val in valSet:
            dupSet.add(node.val)
        else:
            valSet.add(node.val)
        node = node.next
    for val in dupSet:
        head = deleteNode(head,val)
    return(head)

"""
def deleteDups(head):
    valSet = set()
    previous = None
    while(head):
        if head.val in valSet:
            previous.next = head.next
        else:
            valSet.add(head.val)
            previous = head
        head = head.next

def deleteDupsNoDump(head):
    while(head):
        runner = head
        while(runner.next):
            if runner.next.val == head.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        head = head.next


test = Node(5,Node(6,Node(7,Node(6,Node(8)))))
print(test.val,test.next.val,test.next.next.val,test.next.next.next.val,test.next.next.next.next.val)
#res = removeDups(test)
#deleteDups(test)
deleteDupsNoDump(test)
print(test.val,test.next.val,test.next.next.val,test.next.next.next.val)
#print(res.val,res.next.val,res.next.next.val,res.next.next.next.val)