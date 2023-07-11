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

    def bubble_sort(self) :
        ptr = self.head
        cnt = 0
        while ptr is not None :
            cnt += 1
            ptr = ptr.next
        #print(cnt)
        for i in range(1,cnt) :
            curr = self.head
            after = curr.next
            before = curr.prev
            while after is not None :
                if curr.data > after.data :
                    if before == None :
                        before = curr.next
                        after = after.next
                        before.next = curr
                        before.prev = None
                        curr.next = after
                        curr.prev = before
                        self.head = before

                    else :
                        temp = after
                        after = after.next
                        before.next = temp
                        temp.prev = before
                        temp.next = curr
                        curr.prev = temp
                        curr.next = after
                        before = temp
                else :
                    before = curr
                    curr = after
                    after = after.next

llist = List()
llist.create() 
llist.bubble_sort()
llist.traversal()
