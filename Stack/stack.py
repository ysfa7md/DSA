class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class Stack():

    def __init__(self):
        self.top = None
        self.size=0

    def inc_size(self):
        self.size+=1

    def dec_size(self):
        if self.size<1:
            return "list is empty"
        self.size-=1

    def push(self, value):
        node= Node(value)
        if self.top is None:
            self.top=node
        else:
            node.next=self.top
            self.top=node
        self.inc_size()

    def pop(self):
        _top=self.top
        if _top is None:
            raise Exception("Srack is empty!")
        self.top=self.top.next
        self.dec_size()
        return _top

    def to_arr(self):
        _top=self.top
        arr=[]
        while _top:
            arr.insert(0,_top.val)
            _top=_top.next
        return arr

    def __len__(self):
        return self.size

    def __iter__(self):
        _top=self.top
        while _top:
            yield _top.val
            _top=_top.next

    def __repr__(self):
        arr=self.to_arr()
        return "Stack([" + ", ".join(str(x) for x in arr) + "])"

    def __str__(self):
        arr=self.to_arr()
        return "[" + ", ".join(str(x) for x in arr) + "]"

def main():
    stack=Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print("size: ",len(stack))
    print(stack)
    stack.pop()
    print(stack)
    print("size: ",len(stack))

if __name__=='__main__':
    main()
