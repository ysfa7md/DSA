class DynamicArray:
    def __init__(self, cap=2):
        self.cap=cap
        self.size=0
        self.arr=[]

    def size(self):
        ...

    def capacity(self):
        ...

    def is_empty(self):
        ...

    def get(self,index):
        ...

    def set(self,index, value):
        ...

    def append(self,value):
        ...

    def pop(self):
        ...

    def insert(self,index, value):
        ...

    def remove(self,index):
        ...

    def clear(self):
        ...

    def destroy(self):
        ...

    def find(self,value):
        ...

    def contains(self,value):
        ...

    def resize(self,new_capacity):
        ...

