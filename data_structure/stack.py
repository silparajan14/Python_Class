stk = []
size = int(input("enter the size of stack : "))
top = 0
def push():
    global top
    if top == size:
        print("sack is full")
    else:
        el = int(input("enter the element : "))
        stk.append(el)
        top += 1
        print(stk)
def pop():
    global top
    if top == 0:
        print("stack is empty")
    else:
        stk.pop()
        top -= 1
        print(stk)

while True:
    print("operations to perform : ")
    option = int(input("1.push \t\t 2.pop : "))
    if option == 1:
        push()
    elif option == 2:
        pop()
    else:
        print("invalid input.....!")



## global variable :





















