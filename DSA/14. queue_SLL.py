class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def create(self) :
        size = int(input("Enter the size of Queue : "))
        for i in range(size) :
            val = int(input(f"Enter value for Node {i+1} : "))
            self.enqueue(val)

    def enqueue(self, data):
        if self.last is None: #head and last points to the only node
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            print("The list is already empty")
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def isEmpty(self):
        return self.stack == []
        
    def display(self):
        
        ptr = self.head
        if self.isempty():
            raise Exception("\nStack Underflow")
        
        else:
            
            while(ptr != None):
                
                print(ptr.data,"->",end = " ")
                ptr = ptr.next
                if(ptr != None):
                    print(" -> ", end = "")
            return
 
a_queue = Queue()
a_queue.create()
while True:
    print('\n1.enqueue')
    print('2.dequeue')
    print('3.display\n4.quit')
    do = input('Enter your choice : ')
 
    if do == '1':
        val=int(input('Enter value to enqueue : '))
        a_queue.enqueue(val)
        a_queue.display()

    elif do == '2':
        dequeued = a_queue.dequeue()
        if dequeued is None:
            print('\nQueue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
            a_queue.display()
    elif do == '3':
        a_queue.display()

    elif do == '4' :
        break

    else : 
        print("Enter valid choice")
        