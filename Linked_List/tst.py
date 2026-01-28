from linked_list import LinkedList

l=LinkedList()

l.insert_at_tail(3)
l.insert_at_tail(5)
l.insert_at_tail(53)
l.insert_at_tail(99)
l.insert_at_tail(3)
l.insert_at_tail(33)
l.insert_at_head(5)
l.insert_at_head(1)

l.print_list()
l.remove_duplicates()
l.print_list()
print(l.detect_cycle())
# l.make_cycle_at(5,3)
# print(l.detect_cycle())
# l.print_list()

# print(l.search(5))
# print(l.search(1))
# print(l.search(33))
# print(l.search(99))
print(l)
l
