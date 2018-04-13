class BinaryTree():

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def get_root_value(self):
        return self.key

    def insert_left_child(self, root_obj, node = None):
        if node == None:
            node = self
        if node.left_child == None:
            node.left_child = BinaryTree(root_obj)
        else:
            t = BinaryTree(root_obj)
            t.left_child = self.left_child
            node.left_child = t

    def insert_right_child(self, root_obj):
        if self.right_child == None:
            self.right_child = BinaryTree(root_obj)
        else:
            t = BinaryTree(root_obj)
            t.right_child = self.right_child
            self.right_child = t

    def set_root_value(self, value):
        self.key = value

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def append_left_child(self, value, node = None):
        if node == None:
            node = self
        if node.left_child == None:
            node.insert_left_child(value)
            return node
        return self.append_left_child(value, node = node.left_child)

    def append_left_child2(self, value):
        node = self
        while node.left_child != None:
            node = node.left_child
        self.append_left_child(value, node = node)


if __name__ == '__main__':
    main = BinaryTree('a')
    print(main.get_left_child())
    main.insert_left_child('b')
    print(main.get_left_child().get_root_value())
    main.insert_left_child('d')
    print(main.get_left_child().get_root_value())
    print(main.get_left_child().get_left_child().get_root_value())
    main.append_left_child2('e')
    print(main.get_left_child().get_root_value())
    print(main.get_left_child().get_root_value())
    print(main.get_left_child().get_left_child().get_root_value())
    print(main.get_left_child().get_left_child().get_left_child().get_root_value())


