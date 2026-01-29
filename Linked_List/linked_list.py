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

    # O(n) time
    def go_to(self,index):
        ptr=self.head
        for i in range(index):
            ptr=ptr.next
        return ptr

    # O(1) time
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

    # O(1) time
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

    # O(n) time
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

        ptr=self.go_to(index-1) # O(n) time

        ptr2=ptr.next
        ptr.next=node
        node.next=ptr2

        self.inc_size()

    # O(1) time
    def delete_head(self):
        if self.head is None:
            raise Exception("List is empty")

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next

        self.dec_size()

    # O(n) time
    def delete_tail(self):
        if self.tail is None:
            raise Exception("List is empty")

        ptr=self.head

        if self.tail==self.head:
            self.head=None
            self.tail=None
        else:
            ptr=self.go_to(self.size-2) # O(n) time
            self.tail=ptr
            self.tail.next=None
        self.dec_size()

    # O(n) time
    def delete_at_index(self, index):
        if self.head is None:
            raise Exception("List is empty")

        if index >= self.size or index < 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.delete_head()
            return

        prev = self.go_to(index - 1)
        prev.next = prev.next.next
        self.dec_size()


    # # O(n^2) time
    # def remove_duplicates(self):
    #     _set=set()
    #     ptr=self.head
    #     i=0
    #     while ptr:
    #         if ptr.val in _set:
    #             self.delete_at_index(i) # O(n) time
    #             i-=1
    #         else:
    #             _set.add(ptr.val)
    #         i+=1

    #         ptr=ptr.next

    # O(n) time
    def remove_duplicates(self):
        seen = set()
        prev = None
        ptr = self.head

        while ptr:
            if ptr.val in seen:
                prev.next = ptr.next
                self.dec_size()
            else:
                seen.add(ptr.val)
                prev = ptr
            ptr = ptr.next

    # O(n) time
    def search(self,value):
        ptr=self.head
        i=0

        while ptr:
            if ptr.val== value:
                return i
            i+=1
            ptr=ptr.next
        return -1 # not found

    # O(1) time
    def get_length(self):
        return self.size

    # O(1) time
    def is_empty(self):
        # if self.size<1:
        #     return True
        # return False
        return not (self.head or self.tail)

    # O(n) time
    def to_array(self):
        arr = []
        crnt = self.head

        while crnt:
            arr.append(crnt.val)
            crnt = crnt.next

        return arr

    # def print_list(self):
    #     arr=self.to_array()
    #     for i in arr:
    #         print(f'{i}',end='-> ')
    #     print('None')
    #     # print(arr)

    # O(n) time
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

    # O(n) time
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # O(1) time
    def make_cycle(self):
        if not self.head:
            return

        self.tail.next = self.head   # cycle created

    # O(n) time
    def make_cycle_at(self,frm,to):
        if not self.head:
            return
        ptr_from=self.go_to(frm) # O(n) time
        ptr_to=self.go_to(to) # O(n) time

        ptr_from.next=ptr_to

    # O(n) time
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # O(n) time
    def clear(self):
        while not self.is_empty():
            self.delete_head() # O(1) time

    # O(n) time
    def get(self,index):
        if self.head is None:
            raise Exception("List is empty")
        return self.go_to(index).val # O(n) time

# Magic Methods

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        return self.get(index)

    def __setitem__(self,index,value):
        self.insert_at_index(index,value)

    def __delitem__(self,index):
        self.delete_at_index(index)

    def __iter__(self):
        ptr=self.head
        while ptr:
            yield ptr.val
            ptr=ptr.next

    def __contains__(self,value):
        ptr=self.head
        while ptr:
            if ptr.val== value:
                return True
            ptr=ptr.next
        return False

    def __repr__(self):
        arr=self.to_array()
        return "LinkedList([" + ", ".join(str(x) for x in arr) + "])"

    def __str__(self):
        arr=self.to_array()
        return "->".join(str(x) for x in arr) + "->None"


def main():
    ll=LinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    ll.insert_at_tail(3)
    ll.insert_at_tail(2)
    ll.insert_at_tail(1)
    print(len(ll))
    print(ll)
    # ll.reverse()
    # print(ll)
    ll.remove_duplicates()
    print(len(ll))
    print(ll)
    # print(2 in ll)
    # print(20 in ll)

if __name__ == "__main__":
    main()
