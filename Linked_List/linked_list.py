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

    def go_to(self,index):
        ptr=self.head
        for i in range(index):
            ptr=ptr.next
        return ptr

    def insert_at_head(self,value):
        new=Node(value)
        new.next=self.head
        self.head=new
        self.inc_size()

    def insert_at_tail(self, value):
        new = Node(value)

        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.inc_size()


    def insert_at_index(self,index, value):
        if index> self.size:
            return -1

        node=Node(value)
        ptr=self.head
        if index == 0:
            self.insert_at_head(value)
            return
        for _ in range(index-1):
            ptr=ptr.next
        ptr2=ptr.next
        ptr.next=node
        node.next=ptr2
        self.inc_size()

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

        if index>= self.size:
            return -1

        ptr=self.head
        if index == 0:
            self.delete_head()
            return

        for _ in range(index-1):
            ptr=ptr.next

        ptr2=ptr.next
        ptr3=ptr2.next
        ptr.next=ptr3

        del(ptr3)
        self.dec_size()

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
        crnt=self.head
        prev=None

        self.head=self.tail

        while crnt :
            nxt=crnt.next
            crnt.next=prev
            prev=crnt
            crnt=nxt

        self.tail=prev

    # def find_middle(self):
    #     pass

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("slow: ",slow.val)
        print("fast: ",fast.val)
        return slow

    def make_cycle(self):
        if not self.head:
            return

        self.tail.next = self.head   # cycle created

    def make_cycle_at(self,frm,to):
        if not self.head:
            return
        ptr_from=self.go_to(frm)
        ptr_to=self.go_to(to)

        ptr_from.next=ptr_to

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


    def remove_duplicates(self):
        _set=set()
        ptr=self.head
        i=0
        while ptr:
            if ptr.val in _set:
                self.delete_at_index(i)
                i-=1
            else:
                _set.add(ptr.val)

            ptr=ptr.next
            i+=1

    def clear(self):
        while not self.is_empty():
            self.delete_head()





