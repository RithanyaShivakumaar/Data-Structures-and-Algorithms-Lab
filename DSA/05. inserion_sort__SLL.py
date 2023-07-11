class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
class List :
    def __init__(self) :
        self.head = None
    
    def create(self) :
        size = int(input("Enter number of Nodes : "))
        if size ==  0 :
            print("Empty list cannot be created")
            return
        for i in range(size) :
            val = int(input(f"Enter value for Node{i+1} : "))
            self.insert_at_end(val)

    def insert_at_end(self,data) :
        new = Node(data)
        if self.head is None :
            self.head = new
            return  
        ptr = self.head
        while ptr.next is not None :
            ptr = ptr.next
        ptr.next = new 

    def traversal(self) :
        ptr = self.head
        i = 1
        while ptr is not None :
            print(f"Node { i} : ",ptr.data)
            ptr = ptr.next
            i+=1

    def sort(self) :
        tempb=self.head 
        while tempb.next!=None:
            tempa=tempb
            tempc=tempa.next
            x=tempc.data
            while (x < tempa.data and tempa!=tempb.next):
                if tempa==self.head:
                    tempa.next=tempc.next 
                    tempc.next=tempa
                    self.head=tempc 
                else:
                    tempe=self.head
                    while tempe.next!=tempa:
                            tempe=tempe.next
                    tempa.next=tempc.next
                    tempc.next=tempa
                    tempe.next=tempc 
                if tempb==tempa:
                    tempb=tempc
                k=tempa
                tempa=tempc
                tempc=k
                tempf=self.head 
                if tempa!=self.head:
                    while tempf.next!=tempa:
                        tempf=tempf.next
                    tempc=tempa
                    tempa=tempf
                else:
                    tempa=tempb.next
            tempb=tempb.next

llist = List()
llist.create()
llist.sort()
llist.traversal()
        
