class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList():
    def __init__(self, val):
        node=Node(val)
        self.head=node
        self.tail=node
        self.size=1


    def inc_size(self):
        self.size+=1

    def dec_size(self):
        if self.size<1:
            return "list is empty"
        self.size-=1

    def insert_at_head(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new
        self.inc_size()

    def insert_at_tail(self, value):
        new = Node(value)

        if self.tail is None:        # empty list
            self.head = new
            self.tail = new
        else:                        # non-empty list
            self.tail.next = new
            self.tail = new
        self.inc_size()


    def insert_at_index(self,index, value):
        self.inc_size()
        pass

    def delete_head(self):
        _head=self.head

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next

        self.dec_size()
        del(_head)

    def delete_tail(self):
        _tail=self.tail
        crnt=self.head

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            for _ in range(self.size-2):
                crnt=crnt.next
            self.tail=crnt
            self.tail.next=None
        self.dec_size()
        del(_tail)


    def delete_at_index(self,index):
        self.dec_size()
        pass

    def search(self,value):
        ptr=self.head
        i=0

        while True:
            if ptr.val== value:
                return i
            i+=1
            if ptr.next:
                ptr=ptr.next
            else:
                return -1

    def get_length(self):
        return self.size

    def is_empty(self):
        # if self.size<1:
        #     return True
        # return False
        return not (self.head or self.tail)


    def to_array(self):
        arr = []
        crnt = self.head

        while crnt:
            arr.append(crnt.val)
            crnt = crnt.next

        return arr


    def print_list(self):
        arr=self.to_array()
        for i in arr:
            print(f'{i}',end='-> ')
        print('None')
        # print(arr)

    def reverse(self):
        pass

    def find_middle(self):
        pass

    def detect_cycle(self):
        pass

    def remove_duplicates(self):
        pass

    def clear(self):
        while not self.is_empty():
            self.delete_tail()





