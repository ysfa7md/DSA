import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    # ---------- Basic properties ----------

    def test_empty_list(self):
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(len(self.ll), 0)
        self.assertEqual(self.ll.to_array(), [])

    def test_insert_at_head(self):
        self.ll.insert_at_head(10)
        self.ll.insert_at_head(20)
        self.assertEqual(self.ll.to_array(), [20, 10])
        self.assertEqual(len(self.ll), 2)

    def test_insert_at_tail(self):
        self.ll.insert_at_tail(10)
        self.ll.insert_at_tail(20)
        self.assertEqual(self.ll.to_array(), [10, 20])
        self.assertEqual(len(self.ll), 2)

    def test_insert_at_index(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(3)
        self.ll.insert_at_index(1, 2)
        self.assertEqual(self.ll.to_array(), [1, 2, 3])

    def test_insert_at_index_out_of_bounds(self):
        self.ll.insert_at_tail(1)
        with self.assertRaises(IndexError):
            self.ll.insert_at_index(5, 10)

    # ---------- Deletion ----------

    def test_delete_head(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.delete_head()
        self.assertEqual(self.ll.to_array(), [2])
        self.assertEqual(len(self.ll), 1)

    def test_delete_tail(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.delete_tail()
        self.assertEqual(self.ll.to_array(), [1])
        self.assertEqual(len(self.ll), 1)

    def test_delete_at_index(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.ll.delete_at_index(1)
        self.assertEqual(self.ll.to_array(), [1, 3])

    def test_delete_at_index_out_of_bounds(self):
        with self.assertRaises(Exception):
            self.ll.delete_at_index(0)

    # ---------- Search & Access ----------

    def test_search(self):
        self.ll.insert_at_tail(5)
        self.ll.insert_at_tail(10)
        self.assertEqual(self.ll.search(10), 1)
        self.assertEqual(self.ll.search(99), -1)

    def test_get_item(self):
        self.ll.insert_at_tail(7)
        self.ll.insert_at_tail(8)
        self.assertEqual(self.ll[1], 8)

    # ---------- Magic methods ----------

    def test_len_magic(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.assertEqual(len(self.ll), 2)

    def test_contains_magic(self):
        self.ll.insert_at_tail(10)
        self.assertTrue(10 in self.ll)
        self.assertFalse(5 in self.ll)

    def test_iter_magic(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.assertEqual(list(self.ll), [1, 2, 3])

    def test_setitem_magic(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(3)
        self.ll[1] = 2
        self.assertEqual(self.ll.to_array(), [1, 2, 3])

    def test_delitem_magic(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        del self.ll[0]
        self.assertEqual(self.ll.to_array(), [2])

    def test_repr_and_str(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.assertEqual(repr(self.ll), "LinkedList([1, 2])")
        self.assertEqual(str(self.ll), "1->2->None")

    # ---------- Algorithms ----------

    def test_reverse(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.ll.reverse()
        self.assertEqual(self.ll.to_array(), [3, 2, 1])

    def test_find_middle(self):
        for i in range(1, 6):
            self.ll.insert_at_tail(i)
        mid = self.ll.find_middle()
        self.assertEqual(mid.val, 3)

    def test_detect_cycle(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.assertFalse(self.ll.detect_cycle())
        self.ll.make_cycle()
        self.assertTrue(self.ll.detect_cycle())

    def test_remove_duplicates(self):
        for x in [1, 2, 2, 3, 1]:
            self.ll.insert_at_tail(x)
        self.ll.remove_duplicates()
        self.assertEqual(self.ll.to_array(), [1, 2, 3])

    def test_clear(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.clear()
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(len(self.ll), 0)


if __name__ == "__main__":
    unittest.main()
