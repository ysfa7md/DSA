class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList():
    def __init__(self, val):
        self.head=Node(val)
        self.tail=Node(val)
        self.size=1

    def append(self,val):
        self.tail.next=Node(val)
        self.size+=1

    def delete(self,idx):
        ptr=self.head

        for _ in range(idx):
            crnt=ptr.next
        




