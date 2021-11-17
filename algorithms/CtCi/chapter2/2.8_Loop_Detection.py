class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = next

def loopDetection(head):
    setPointer = set()
    while(head):
        if head in setPointer:
            return head
        setPointer.add(head)
        head = head.next
    return None

test = Node(1,Node(2,Node(3,Node(4,Node(5)))))
test.next.next.next.next.next = test.next

res = loopDetection(test)
if res == None:
    print('No Loop Detected')
else:
    print(res.val)