import time
import sys

def push(item):
    global topPointer
    if topPointer < stackFull -1:
        topPointer = topPointer + 1
        myStack[topPointer] = item
    else:
        print("⚠Stack is full, cannot push⚠")

def pop(item):
    global topPointer
    global basePointer
    if topPointer == basePointer - 1:
        print("⚠Stack is empty, cannot pop⚠")
    else:
        myStack[topPointer] = item
        topPointer = topPointer - 1

UBound = int(input("input the maximum size of the stack\n"))
myStack = [None for i in range(0,UBound)]
basePointer = 0
topPointer = -1
stackFull = UBound

print("================\nCurrent Stack\n"+str(myStack)+"\n================\n")
while topPointer <= stackFull:
    time.sleep(1)
    option = int(input("Choose an action to perform on the stack 1/2/3/4 :\n1. Push(Add element)\n2. Pop(Remove an element)\n3. Peek(Display Stack)\n4. Exit\n"))

    if option == 1:
        item = int(input("Input the item to push\n"))
        push(item)
        time.sleep(1)
        print("================\nCurrent Stack\n"+str(myStack)+"\n================\n")
    elif option == 2:
        item = None
        pop(item)
        time.sleep(1)
        print("================\nCurrent Stack\n"+str(myStack)+"\n================\n")
    elif option == 3:
        time.sleep(1)
        print("================\nCurrent Stack\n"+str(myStack)+"\n================\n")
    elif option == 4:
        sys.exit()
    else:
        print("Invalid Option, Please input 1, 2 or 3\n")