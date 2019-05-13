class Node(object):
    def __init__(self, value):
        self.value = value
        self.pre = None


class Stack(object):

    def __init__(self):
        self.stack = None

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.stack = node
        else:
            node.pre = self.stack
            self.stack = node

    def pop(self):
        node = self.stack
        self.stack = node.pre
        return node.value

    def peek(self):
        return self.stack.value

    def is_empty(self):
        return not self.stack


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
