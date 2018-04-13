import unittest
import linked_list
import node

class TestAddList(unittest.TestCase):

    def setUp(self):
        l1 = linked_list.LinkedList()
        l1.add_node(7)
        l1.add_node(1)
        l1.add_node(6)
        l1.add_node(6)
        l1.add_node(8)

        l2 = linked_list.LinkedList()
        l2.add_node(2)
        l2.add_node(1)
        l2.add_node(9)
        self.l1 = l1
        self.l2 = l2

    def test_not_sure(self):
        n = get_last_node(self.l1.get_head())
        print(n.data)

def get_last_node(current):
    n = None
    if current.next == None:
        return current
    else:
        n=  get_last_node(current.next)
    print("here {d}".format(d = n.data))
    n.data += 1
    return n


if __name__ == '__main__':
    unittest.main()
