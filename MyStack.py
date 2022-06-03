class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        temp = self.stack[-1]
        self.stack.pop()
        return temp

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
