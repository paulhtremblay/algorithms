class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class MyList:

    def __init__(self):
        self.head = None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

class MyHash:

    def __init__(self):
        self.list = [None for i in range(299)]

    def gen_hash_value(self, s):
        g = 0
        for i in s:
            g += ord(i)
        return g % 300 

    def add(self, key, data):
        h = self.gen_hash_value(key)
        i = self.list[h]
        if i == None:
            i = MyList()
        i.add([key, data])
        self.list[h] = i

    def get_item(self, key):
        h = self.gen_hash_value(key)
        l = self.list[h]
        if l == None:
            return None
        n = l.head
        while True:
            k = n.data[0]
            if k == key:
                return n.data[1]
            if n == None:
                return None
            n = n.next
        raise ValueError("should not happen")


if __name__ == '__main__':
    h = MyHash()
    h.add('foo', 'this is foo')
    h.add('fpn', 'this is not foo')
    a = h.get_item('foo')
    b = h.get_item('fpn')
    c = h.get_item('fmn')
    d = h.get_item('f')
    print(a, b, c, d)

