import time
#import 
start = time.time()
class Node :
    def __init__(self,data) :
        self.prev = None
        self.data = data
        self.next = None

class List :
    def __init__(self) :
        self.head = None 

    def create(self) :
        size = int(input("Enter the number of nodes : "))
        if size == 0 :
            print("You cannot create an empty list")
            return
        for i in range (size) :
            val = int(input(f"Enter value for Node {i+1} : "))
            self.insert_at_end(val)

    def insert_at_end(self,data) :
        if self.head is None :
            new = Node(data)
            self.head = new
            return
        ptr = self.head
        while ptr.next is not None :
            ptr = ptr.next
        new = Node(data)
        ptr.next = new
        new.prev = ptr

    def traversal(self) :
        if self.head is None :
            print("The list is empty")
            return
        else :
            ptr = self.head 
            i = 1
            while ptr is not None :
                print(f"Node {i} : ",ptr.data)
                ptr = ptr.next
                i+=1

    def insertsort(self):
        tempb=self.head 
        while tempb.next!=None:
            tempa=tempb
            tempc=tempa.next
            x=tempc.data
            while (x > tempa.data and tempa!=tempb.next):
                if tempa==self.head:
                    x1=tempc.next
                    tempa.next=x1
                    x1.prev=tempa
                    tempc.next=tempa
                    tempa.prev=tempc
                    self.head=tempc
                elif tempc.next==None:
                    tempe=tempa.prev
                    tempa.next=None
                    tempc.next=tempa
                    tempa.prev=tempc
                    tempe.next=tempc
                    tempc.prev=tempe
                else:
                    tempe=self.head
                    while tempe.next!=tempa:
                        tempe=tempe.next
                    x1=tempc.next
                    tempa.next=x1
                    x1.prev=tempa
                    tempc.next=tempa
                    tempa.prev=tempc
                    tempe.next=tempc
                    tempc.prev=tempe
                if tempb==tempa:
                    tempb=tempc
                k=tempa
                tempa=tempc
                tempc=k
                tempf=self.head 
                if tempa!=self.head:
                    tempf=tempa.prev
                    tempc=tempa
                    tempa=tempf
                else:
                    tempa=tempb.next
            tempb=tempb.next
end = time.time()

llist = List()
llist.create()
print("Before Sorting : ")
llist.traversal()
llist.insertsort()
print("\nAfter Sorting : ")
llist.traversal()
print("The time complexity calculated : ",end - start)
            
