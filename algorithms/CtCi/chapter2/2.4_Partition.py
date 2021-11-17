class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

def partition(head,val):
    runner = head
    while(runner):
        while(head.val < val):
            if not head.next:
                return 
            head = head.next
            runner = head.next.next
        if runner.val < val:
            temp = runner.val
            runner.val = head.val
            head.val = temp
        runner = runner.next
     

test = Node(3,Node(5,Node(8,Node(5,Node(10,Node(2,Node(1)))))))
print(test.val,test.next.val,test.next.next.val,test.next.next.next.val,test.next.next.next.next.val,test.next.next.next.next.next.val,test.next.next.next.next.next.next.val)
partition(test,7)
print(test.val,test.next.val,test.next.next.val,test.next.next.next.val,test.next.next.next.next.val,test.next.next.next.next.next.val,test.next.next.next.next.next.next.val)