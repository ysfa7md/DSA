class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

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
