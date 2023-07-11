class Node:
    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
 
class Stack:
 
    # head is default NULL
    def __init__(self):
        self.head = None
 
    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def create(self) :
        size = int(input("Enter the size of Stack : "))
        for i in range(size) :
            val = int(input(f"Enter value for Node {i+1} : "))
            self.push(val)
 
    # Method to add data to the stack
    # adds to the start of the stack
    #no need to check if the list is full, as her it is dynamic allocation
    def push(self,data):
 
        if self.head == None:
            self.head = Node(data)
 
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head.prev = newnode
            newnode.prev = None
            self.head = newnode
 
    # Remove element that is the current head (start of the stack)
    def pop(self):
 
        if self.isempty():
            print("List is already empty")
            return None
 
        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None #first node is deleted
            self.head.prev = None
            return poppednode.data
 
    # Returns the head node data
    def peek(self):
 
        if self.isempty():
            return None
 
        else:
            return self.head.data
 
    # Prints out the stack
    def display(self):
 
        ptr = self.head
        if self.isempty():
            raise Exception ("Stack Underflow")
 
        else:
 
            while(ptr != None):
 
                print(ptr.data, end = "")
                ptr = ptr.next
                if(ptr != None):
                    print(" -> ", end = "")
            return

s = Stack()
s.create()
while(True):
    ele = int(input("\n1 Push\n2 Pop\n3 to check if it is Empty\n4 Print Stack\n5 Exit\nEnter your choice : "))
    if(ele == 1):
        item = input("Enter Element to push into the stack : ")
        s.push(item)
        s.display()

    if(ele == 2):
        print("Element popped : ",s.pop())
        s.display()

    if(ele == 3):
        print(s.isEmpty())

    if(ele == 4):
        s.printStack()

    if(ele == 5):
        break
