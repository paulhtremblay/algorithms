import pprint
pp = pprint.PrettyPrinter(indent = 4)
class GenericStack():
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

class ParagraphStack(GenericStack):
    pass


class InlineStack(GenericStack):
    pass

class Token:

    def __init__(self, the_type, value):
        self.type = the_type
        self.value = value

def pop_until_inline(inline_stack):
    pass

def convert(tokens):
    """
    \b bold text \i italics \p
    {\b bold text {\i italics}} \p

    """
    inline_stack = InlineStack()
    final = []
    for token in tokens:
        if token.type == 'text':
            inline_stack.push(token)
        elif token.type == 'open_bracket':
            inline_stack.push(token)
        elif token.type == 'inline':
            pop_until_inline(inline_stack)
        print(token.value)
    return final


if __name__ == '__main__':
    t1 = Token('text', 'Start text')
    t2 = Token('text', 'End text')
    t3 = Token('text', 'bold')
    b1 = Token('inline', '\\b')
    br1 = Token('open_bracket', '{')
    br2 = Token('close_bracket', '}')
    f = convert([t1, br1, b1, t3, br2, t2]) 
    pp.pprint(f)
