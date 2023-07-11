class Node :
    def __init__(self,data) :
        self.data = data
        self.link = None

class Stack :
    def __init__(self) :
        self.head = None

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

    def push(self, data):
 
        if self.head == None:
            self.head = Node(data)
 
        else:
            newnode = Node(data)
            newnode.link = self.head
            self.head = newnode

    def pop(self):
 
        if self.isempty():
            print("List is already empty")
            return None
 
        else:
            poppednode = self.head
            self.head = self.head.link
            poppednode.link = None 
            return poppednode.data

    def display(self):
 
        ptr = self.head
        if self.isempty():
            raise Exception ("Stack Underflow")
 
        else:
 
            while(ptr != None):
 
                print(ptr.data, end = "")
                ptr = ptr.link
                if(ptr != None):
                    print(" -> ", end = "")
            return

    def delete(self,key) :
        temp = []
        ptr = self.head
        while (ptr.data != key and ptr is not None) :
            temp.append(ptr.data)
            tmp = self.head
            self.head = self.head.link
            ptr = ptr.link
            tmp.link = None
        
        if self.isempty() :
            print("Element specified is not present in the list")
            return

        else :
            print(temp)
            tmp = self.head
            self.head = self.head.link
            tmp.link = None
            while(len(temp) != 0) :
                new = Node(temp[-1])
                new.link = self.head
                self.head = new
                temp.pop(-1)

stk = Stack()
stk.create()
while True:
    print('\n1.Push \n2.Pop \n3.Delete \n4.Quit')
    choice = int(input('Enter your choice : '))
 
    if choice == 1 :
        val = int(input('Enter value to Push : '))
        stk.push(val)
        stk.display()

    elif choice == 2 :
        ele = stk.pop()
        if ele is None:
            print('\nStack is empty.')
        else:
            print('Popped Element : ', int(ele))
            stk.display()
    elif choice == 3 :
        key = int(input("Enter an element to delete : "))
        stk.delete(key)
        stk.display()
        
    elif choice == 4 :
        break

    else : 
        print("Enter valid choice")

