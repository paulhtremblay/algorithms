def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def factorial_with_stack(n):
    stack = Stack()
    while n != 1:
        stack.push(n)
        n -= 1
    final = 1
    while stack.size() != 0:
        final = final * stack.pop()
    return final


print(factorial(5))
print(factorial_with_stack(5))
