import unittest
import node

class TestSingleLinkedList(unittest.TestCase):

    def setUp(self):
        self.single_list = SingleList()

    def test_insert_a_single_node(self):
        self.single_list.insert_item_at_0_pos('a')
        self.assertEqual(self.single_list.size, 1)
        self.assertEqual(self.single_list.peek_at_head().data, 'a')

    def test_insert_2_nodes(self):
        self.single_list.insert_item_at_0_pos('a')
        self.single_list.insert_item_at_0_pos('b')
        self.assertEqual(self.single_list.size, 2)
        self.assertEqual(self.single_list.peek_at_head().data, 'b')

    def test_insert_2_nodes_get_head(self):
        self.single_list.insert_item_at_0_pos('a')
        self.single_list.insert_item_at_0_pos('b')
        self.assertEqual(self.single_list.get_head().data, 'b')
        self.assertEqual(self.single_list.peek_at_head().data, 'a')
        self.assertEqual(self.single_list.size, 1)

    def test_generator(self):
        self.single_list.insert_item_at_0_pos('a')
        self.single_list.insert_item_at_0_pos('b')
        counter = 0
        for d in self.single_list.iterate_through_list():
            counter += 1
        self.assertEqual(counter, 2)

    def test_generator2(self):
        counter = 0
        for d in self.single_list.iterate_through_list():
            counter += 1
        self.assertEqual(counter, 0)

class SingleList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_item_at_0_pos(self, data):
        temp = self.head
        new_node = node.Node(data)
        new_node.set_next(temp)
        self.head = new_node
        self.size += 1

    def peek_at_head(self):
        return self.head

    def get_head(self):
        the_next = self.head.next
        temp = self.head
        self.head = the_next
        self.size -= 1
        return temp

    def iterate_through_list(self):
        the_next = self.head
        while the_next != None:
            yield the_next
            the_next = the_next.next

if __name__ == '__main__':
    unittest.main()
