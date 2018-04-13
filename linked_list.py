import unittest
import node

class TestLinkedList(unittest.TestCase):

    def test_add_1_node(self):
        l = LinkedList()
        l.add_node('a')
        self.assertEqual(l.get_head().data, 'a')

    def test_add_2_node(self):
        l = LinkedList()
        l.add_node('a')
        l.add_node('b')
        self.assertEqual(l.get_head().next.data, 'b')

    def test_add_3_node(self):
        l = LinkedList()
        l.add_node('a')
        l.add_node('b')
        l.add_node('c')
        self.assertEqual(l.get_head().next.next.data, 'c')

    def test_iterate_through_list1(self):
        l = LinkedList()
        l.add_node('a')
        l.add_node('b')
        l.add_node('c')
        my_gen = l.iterate_through_list()
        for i in my_gen:
            print(i.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def add_node(self, data):
        _node = node.Node(data)
        if self.head == None:
            self.head = _node
            _node.next = None
        else:
            current_node = self.head
            while True:
                if current_node.next== None:
                    current_node.next = _node
                    break
                current_node = current_node.next

    def iterate_through_list(self):
        current_node = self.head
        while current_node != None:
            yield current_node
            current_node = current_node.next


if __name__ == '__main__':
    unittest.main()
