class Node :
    def __init__(self,data) :
        self.data = data
        self.link = None

class List :
    def __init__(self) :
        self.head = None 
    
    def create(self) :
        size = int(input("Enter the total number of nodes : "))
        if size == 0 :
            print("Empty list cannot be created")
            return
        for i in range(size) :
            val = int(input(f"Enter value for Node {i+1} : "))
            self.insert_at_end(val)

    def insert_at_end(self, data) :
        new = Node(data)
        if self.head is None :
            self.head = new
            return  
        ptr = self.head
        while ptr.link is not None :
            ptr = ptr.link 
        ptr.link = new 

    def traversal(self) :
        if self.head is None :
            print("the list is empty")
            return
        else :
            ptr = self.head
            i = 1
            while ptr is not None :
                print(f"Node {i} : ",ptr.data)
                ptr = ptr.link
                i+=1

    def bubble_sort(self) :
        ptr = self.head
        cnt = 1
        while ptr is not None :
            ptr = ptr.link
            cnt+=1
        print(cnt)
        
        for i in range(1,cnt): #for controlling passes of Bubble Sort
            curr = self.head
            nxt = curr.link
            prev = None
            while nxt is not None : #Comparisons in passes
                if curr.data > nxt.data: 
                    if prev == None: #if the first node has to be swapped
                       prev = curr.link
                       nxt = nxt.link
                       prev.link = curr
                       curr.link = nxt
                       self.head = prev
                    else:    #in case of in between nodes
                        temp = nxt
                        nxt = nxt.link
                        prev.link = curr.link
                        prev = temp
                        temp.link = curr
                        curr.link = nxt
                else:           
                    prev = curr
                    curr = nxt
                    nxt = nxt.link

llist = List()
llist.create() 
llist.bubble_sort()
llist.traversal()

