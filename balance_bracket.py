from MyStack import Stack


def balanced(s):
    stack = Stack()
    bracket_open = '([{'
    bracket_close = ')]}'
    is_good = True
    for b in s:
        if b in bracket_open:
            stack.push(b)
        elif b in bracket_close:
            if stack.isEmpty():
                is_good = False
                break
            top_bracket = stack.pop()
            if top_bracket == '(' and b == ')':
                continue
            if top_bracket == '[' and b == ']':
                continue
            if top_bracket == '{' and b == '}':
                continue
            else:
                break
    if is_good and stack.size() == 0:
        print('Сбалинсировано')
    else:
        print('Несбалансировано')


print(balanced(input()))
