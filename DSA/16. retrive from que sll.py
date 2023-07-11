class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def dequeue(self):
        if self.head != None:
            node = self.head 
            self.head = self.head.next
            return node
        else :
            print("underflow")
            self.tail = None
    
    def retrive(self):
        val = int(input("Enter the value to be retrived: "))
        end = self.head
        while self.head.data != val:
            node = l.dequeue()
            node1 = l.enqueue(node.data)
    
        new = self.head 
        self.head = self.head.next 
    
        while self.head.data != end.data:
            node = l.dequeue()
            node1 = l.enqueue(node.data)
  
    def display(self):
        temp = self.head 
        print("\nQueue Display : ",end = "")
        while temp is not None:
            print(temp.data,end = "  ")
            temp = temp.next
            if (temp != None) :
                print("->",end = " ")
        return
    

l = sll_queue()
while True:
    print("\n1.Enqueue \n2.Dequeue \n3.Delete and retrieve \n4.Exit")
    ch = int(input("\nEnter the operation you want to perform: "))
    if ch == 1:
        data = int(input("Enter the value you want to insert: "))
        temp = l.enqueue(data)
        l.display()
    if ch == 2:
        temp = l.dequeue()
        l.dislay()
    if ch == 3:
        l.retrive()
        l.display()
    if ch == 4:
        break