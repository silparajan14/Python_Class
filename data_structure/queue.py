# only difference :stk.pop(0) instead of stk.pop()

stk = []
size = int(input("enter the size of stack : "))
top = 0
def enqueue():
    global top
    if top == size:
        print("sack is full")
    else:
        el = int(input("enter the element : "))
        stk.append(el)
        top += 1
        print(stk)
def dequeue():
    global top
    if top == 0:
        print("stack is empty")
    else:
        stk.pop(0)
        top -= 1
        print(stk)

while True:
    print("operations to perform : ")
    option = int(input("1.push \t\t 2.pop : "))
    if option == 1:
        enqueue()
    elif option == 2:
        dequeue()
    else:
        print("invalid input.....!")

