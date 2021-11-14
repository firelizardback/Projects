class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def kth2Last(head,k):
    runner = head
    i = 0
    while(runner):
        if (i > k):
            head = head.next
        runner = runner.next
        i += 1      
    if i <= k: 
        return None
    else:
        return head.val

test = Node(5,Node(6,Node(7,Node(6,Node(8)))))
print(kth2Last(test,5))