class Stack:
    def __init__(self):
        self.stack = []

    def create(self) :
        size = int(input("Enter the size of Stack : "))
        for i in range(size) :
            val = int(input(f"Enter value for index {i+1} : "))
            self.push(val)

    #Method to append the element in the stack at top position.
    def push(self, element):
        self.stack.append(element)

    #Method to Pop last element from the top of the stack
    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1] #Save the last element to return
            del(self.stack[-1]) #Remove the last element
            return lastElement
        else:
            return("Stack Already Empty")

    #Method to check if stack is empty or not
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)

s = Stack()
s.create()
while(True):
    ele = int(input("1 for Push\n2 for Pop\n3 to check if it is Empty\n4 to print Stack\n5 to exit\nEnter your choice : "))
    if(ele == 1):
        item = input("Enter Element to push in stack : ")
        s.push(item)
    if(ele == 2):
        print(s.pop())
    if(ele == 3):
        print(s.isEmpty())
    if(ele == 4):
        s.printStack()
    if(ele == 5):
        break
