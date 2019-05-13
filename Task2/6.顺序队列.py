class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def is_empty(self):
        return not self.stack


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.peek())
