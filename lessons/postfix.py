stack = []
# push n -> ok
def push(n):
  stack.append(n)
# pop -> n
def pop():
  n = stack.pop()
  return n
# back -> n
def back():
  return(stack[-1])
# size -> len
def size():
  return len(stack)
# clear -> ok
def clear():
  stack.clear()
def is_empty():
  return len(stack) == 0

st = input().split()
for s in st:
    if s == '+':
        b = pop()
        a = pop()
        push(a+b)
    elif s == '-':
        b = pop()
        a = pop()
        push(a-b)
    elif s == '*':
        b = pop()
        a = pop()
        push(a*b)
    else:
        n = int(s)
        push(n)
    #print(s, stack)

print(pop())

