class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None


def correct_bracket(string):
    stack = Stack()
    for bracket in string:
        if bracket in "([{":
            stack.push(bracket)
        elif bracket in "}])":
            if stack.is_empty():
                return False
            if (bracket == ")" and stack.peek() == "(") or \
                    (bracket == "}" and stack.peek() == "{") or \
                    (bracket == "]" and stack.peek() == "["):
                stack.pop()
            else:
                return False
    return stack.is_empty()


print(correct_bracket("(){[()]}"))
