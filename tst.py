from linked_list import LinkedList

l=LinkedList(4)

l.insert_at_tail(3)
l.insert_at_tail(5)
l.insert_at_head(5)
l.insert_at_head(1)
l.print_list()
# l.delete_head()
l.print_list()
print(l.search(5))
print(l.search(3))
