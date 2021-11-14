class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def deleteMiddleNode(node):
    if not node:
        return
    if not node.next:
        return
    node.val = node.next.val
    node.next = node.next.next


test = Node(5,Node(6,Node(7,Node(6,Node(8)))))
deleteMiddleNode(test.next.next.next)
print(test.val,test.next.val,test.next.next.val,test.next.next.next.val)
