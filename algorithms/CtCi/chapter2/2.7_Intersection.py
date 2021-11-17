class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = next

def intersection(head1,head2):
    setPointer = set()
    while(head1):
        setPointer.add(head1)
        head1 = head1.next
    while(head2):
        if head2 in setPointer:
            return head2
        head2 = head2.next
    return None

test = Node(5,Node(6,Node(9,Node(6,Node(5)))))
test1 = Node(7,Node(8,test))
test2 = Node(10,Node(12,test))

res = intersection(test1,test2)
if res == None:
    print('No intersection')
else:
    print(res.val)
