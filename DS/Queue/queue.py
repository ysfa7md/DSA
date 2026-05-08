class Node:
    def __init__(self, value):
        self.val = value
        self.next = None



# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.start = None
#         self.end = None
#         self.cap = k
#         self.size = 0

#     def inc_size(self):
#         self.size += 1

#     def dec_size(self):
#         if self.size > 0:
#             self.size -= 1

#     def enQueue(self, value: int) -> bool:
#         node = Node(value)
#         if self.isFull():
#             return False
#         if self.start is None:
#             self.start = node
#             self.end = node
#             node.next = node
#         else:
#             self.end.next = node
#             self.end = node
#             self.end.next = self.start

#         self.inc_size()
#         return True

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False

#         if self.size == 1:
#             self.start = None
#             self.end = None
#         else:
#             self.start = self.start.next
#             self.end.next = self.start
#         self.dec_size()

#         return True

#     def Front(self) -> int:
#         if self.start:
#             return self.start.val
#         return -1

#     def Rear(self) -> int:
#         if not self.start:
#             return -1
#         return self.end.val

#     def isEmpty(self) -> bool:
#         return self.size == 0

#     def isFull(self) -> bool:
#         return self.size == self.cap

class Queue():
    def __init__(self):
        self.start=None
        self.end=None
        self.size=0

    def inc_size(self):
        self.size+=1

    def dec_size(self):
        if self.size<1:
            return "list is empty"
        self.size-=1

    def inque(self, value):
        node=Node(value)
        if self.start is None:
            self.start =node
            self.end =node
        else:
            self.end.next = node
            self.end=node

        self.inc_size()

    def deque(self):
        if self.end is None:
            raise Exception("Queue is empty")

        top= self.start
        if not self.start.next:
            self.start=None
            self.end=None
        else:
            self.start=self.start.next
        self.dec_size()

        return top

    def top(self):
        if self.start is Node:
            raise Exception("Queue is empty")
        return self.start

    def to_arr(self):
        top=self.start
        arr=[]
        while top:
            arr.append(top.val)
            top=top.next
        return arr

    def __len__(self):
        return self.size

    def __iter__(self):
        top=self.start
        while top:
            yield top.val
            top=top.next

    def __repr__(self):
        arr = self.to_arr()
        return f'Queue([{','.join(str(x) for x in arr)}])'

    def __str__(self):
        arr = self.to_arr()

        return f'[{','.join(str(x) for x in arr)}]'

def main():
    queue=Queue()
    queue.inque(1)
    queue.inque(2)
    queue.inque(3)
    queue.inque(3)
    print(queue)
    print(len(queue))

    queue.deque()
    print(queue)

    queue.deque()
    print(queue)

    queue.deque()
    print(queue)
    print(len(queue))

if __name__=='__main__':
    main()
