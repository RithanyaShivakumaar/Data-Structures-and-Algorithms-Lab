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

    def insert_at_index(self,index,data) :
        if index == 1 :
            new = Node(data)
            new.next = self.head
            self.head.prev = new
            self.head = new
            return
        ptr = self.head
        i = 1
        while i < index - 1 and ptr is not None :
            ptr = ptr.next
            i+=1
        if ptr is None :
            print("The index specified is out of bounce")
        else :
            new = Node(data)
            new.next = ptr.next
            new.prev = ptr
            ptr.next.prev = new
            ptr.next = new

    def insert_after_value(self,data,x) :
        ptr = self.head 
        while ptr.next is not None :
            if ptr.data == x :
                break
            ptr = ptr.next
        if ptr is None :
            print("The value specified is not present in the list")
        else : 
            new = Node(data)
            new.next = ptr.next
            new.prev = ptr
            if ptr.next is not None : 
                ptr.next.prev = new
            ptr.next = new

    def delete(self,x) :
        if self.head is None :
            print("The list is empty")
            return
        if self.head.data == x : 
            self.head = self.head.next
            self.head.prev = None
            return
        
        ptr = self.head
        while ptr.next is not None :
            if ptr.data == x :
                break
            ptr = ptr.next
        if ptr.next is None :
            if ptr.item == x :
                ptr.prev.next = None
            else :
                print("The element specified is not present in the list")
        else :
            ptr.prev.next = ptr.next
            ptr.next.prev = ptr.prev

    def reverse(self) :
        if self.head is None :
            print("The list is empty")
            return
        p1 = self.head
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None :
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.head = p1

    def Reverse(self) :
        ptr = self.head
        while ptr.next is not None :
            ptr = ptr.next
        while ptr is not None :
            print(ptr.data)
            ptr = ptr.prev

llist = List()
llist.create()

print("\n1.Insert at index \n2.Insert by value \n3.Delete \n4.Traversal \n5.Reverse \n6.Exit") 
choice = int(input("Enter your choice : "))

while choice != 6 :
    if choice == 1 :
        pos = int(input("Enter the position for it : "))
        ele = int(input("Enter the value that needs to be inserted : "))
        llist.insert_at_index(pos,ele)
        llist.traversal()
    elif choice == 2 :
        ele = int(input("Enter the value that needs to be inserted : "))
        val = int(input("Enter the value after which it needs to be inserted : "))
        llist.insert_after_value(ele,val)
        llist.traversal()
    elif choice == 3 :
        ele = int(input("Enter the value that needs to be deleted : "))
        llist.delete(ele)
        llist.traversal()
    elif choice == 4 :
        llist.traversal()
    elif choice == 5 :
        llist.Reverse()
    elif choice == 6 :
        exit()
    else : 
        print("Enter valid Choice")
        
    print("\n1.Insert at index \n2.Insert by value \n3.Delete \n4.Traversal \n5.Reverse \n6.Exit") 
    choice = int(input("Enter your choice : "))
            
