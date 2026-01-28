class Node:
    def __init__(self,value):
        self.val=value
        self.next=None


class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

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
        node=Node(value)

        if self.head is None:
            self.head=node
            self.tail=self.head
            self.inc_size()
            return

        node.next=self.head
        self.head=node
        self.inc_size()

    def insert_at_tail(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail=node
            self.head=self.tail
            self.inc_size()
            return

        self.tail.next = node
        self.tail = node
        self.inc_size()


    def insert_at_index(self,index, value):
        if self.head is None or index==self.size:
            self.insert_at_tail(value)
            return

        if index> self.size:
            raise IndexError("Index out of bounds")

        node=Node(value)
        ptr=self.head
        if index == 0:
            self.insert_at_head(value)
            return

        ptr=self.go_to(index-1)

        ptr2=ptr.next
        ptr.next=node
        node.next=ptr2

        self.inc_size()

    def delete_head(self):
        if self.head is None:
            raise Exception("List is empty")

        _head=self.head

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next

        self.dec_size()
        del(_head)

    def delete_tail(self):
        if self.tail is None:
            raise Exception("List is empty")

        _tail=self.tail
        ptr=self.head

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            ptr=self.go_to(self.size-2)
            self.tail=ptr
            self.tail.next=None
        self.dec_size()
        del(_tail)


    def delete_at_index(self,index):
        if self.head is None:
            raise Exception("List is empty")

        if index >= self.size:
            raise IndexError("Index out of bounds")

        ptr=self.head

        if index == 0:
            self.delete_head()
            return

        ptr=self.go_to(index-1)

        ptr2=ptr.next
        ptr3=ptr2.next
        ptr.next=ptr3

        del(ptr3)
        self.dec_size()

    def search(self,value):
        ptr=self.head
        i=0

        while ptr:
            if ptr.val== value:
                return i
            i+=1
            ptr=ptr.next
        return -1 # not found

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

# Magic Methods

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        if index>=self.size:
            raise IndexError("Index out of bounds")
        ptr=self.go_to(index)
        return ptr.val

    def __setitem__(self,index,value):
        if index>=self.size:
            raise IndexError("Index out of bounds")
        ptr=self.go_to(index)
        ptr.val=value

    def __delitem__(self,index):
        if index>=self.size:
            raise IndexError("Index out of bounds")
        self.delete_at_index(index)

    def __iter__(self):
        ptr=self.head
        while ptr:
            yield ptr.val
            ptr=ptr.next

    def __repr__(self):
        arr=self.to_array()
        return "LinkedList([" + ", ".join(str(x) for x in arr) + "])"

    def __str__(self):
        arr=self.to_array()
        return "->".join(str(x) for x in arr) + "->None"

    def __contains__(self,value):
        ptr=self.head
        while ptr:
            if ptr.val== value:
                return True
            ptr=ptr.next
        return False
