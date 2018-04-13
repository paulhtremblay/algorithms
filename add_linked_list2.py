import unittest
import linked_list
import node

class TestAddList(unittest.TestCase):

    def setUp(self):
        l1 = linked_list.LinkedList()
        l1.add_node(7)
        l1.add_node(1)
        l1.add_node(6)

        l2 = linked_list.LinkedList()
        l2.add_node(2)
        l2.add_node(1)
        l2.add_node(9)
        self.l1 = l1
        self.l2 = l2

    def test_not_sure(self):
        n = add_linked_list(self.l1.get_head(), self.l2.get_head(), 0)
        print('raw sum is {the_sum}'.format(the_sum = 617 + 912))
        current = n
        while current != None:
            print(current.data)
            current = current.next

def add_linked_list(node1, node2, remainder):
    value = remainder
    if node1 != None:
        value += node1.data
    if node2 != None:
        value += node2.data
    result = node.Node(value % 10)
    print("up at top and result is {r}".format(r = result))
    if node1 != None or node2 != None or remainder != 0:
        next1 = None
        next2 = None
        if  node1 != None:
            next1 = node1.next
        if  node2 != None:
            next2 = node2.next
        if value > 9:
            remainder = 1
        else:
            remainder = 0
        more = add_linked_list(next1, next2, remainder)
        # stack is [ Set result.next(more),
        #set result.next to previous
        #set result.next to previous
        print("after stack and result is {d}".format(d = result))
        print("after stack and node for more is data is {d}".format(d = more))
        result.set_next(more)
    return result


if __name__ == '__main__':
    unittest.main()
