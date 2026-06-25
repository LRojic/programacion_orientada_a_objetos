stack = []

stack.append(5)
stack.append(3)

print(stack.pop())   # 3

stack.append(2)
stack.append(8)

print(stack.pop())   # 8
print(stack.pop())   # 2

stack.append(9)
stack.append(1)

print(stack.pop())   # 1

stack.append(7)
stack.append(6)

print(stack.pop())   # 6
print(stack.pop())   # 7

stack.append(4)

print(stack.pop())   # 4
print(stack.pop())   # 9

print("Stack final:", stack)