#reverse string 
# str = "hello"
# output = 


def reverse(s:str):
    stack = []
    result = ""
    for char in s:
        stack.append(char)
    for i in range(len(stack)):
        eachChar = stack.pop()
        result += eachChar
    return result

print(reverse("hello"))



#using python slicing method to reverse string 
def sliceReverce(s):
    return s[::-1]

print(sliceReverce("python slicing"))



n = 5
stack = [None] * n
top1 = -1
top2 = n

#push element to stack 1
def push1(x):
    if top1 < top2 - 1:
        top1 += 1
        stack[top1] = x
    else:
        raise Exception("Stack overflowed")


def push2(x): 
    if top1 < top2 -1:
        top2 -= 1
        stack[top2] = x
    else:
        raise Exception("Stack overflowed again")


def pop1():
    if top1 > -1:
        popped =stack[top1]
        stack[top1] = None
        top1 -= 1
        return popped
    else:
        raise Exception("There is nothing to pop")

def pop2():
    if top2 < n - 1:
        popped = stack[top2]
        stack[top2] = None
        top2 +=1
        return popped
    else:
        raise Exception("There is nothing to pop again")