class LinkNode :
    def __init__(self, data) :
        self.data = data
        self.next = None

class SingleLL :
    head = None
    def __init__(self) :
        self.head = None
    # Add new Node at end of linked list
    def addNode(self, data) : 
        node = LinkNode(data)
        if (self.head == None) :
            self.head = node
        else :
            temp = self.head
            # Find the last node
            while (temp.next != None) :
                temp = temp.next
            # Append the node at last position
            temp.next = node
    # Display linked list element
    def display(self) :
        if (self.head == None) :
            print("\n Empty linked list")
            return
        temp = self.head
        # iterating linked list elements
        while (temp != None) :
            if (temp != self.head) :
                print(end = "→ ")
            print(temp.data, end =" ")
            # Visit to next node
            temp = temp.next
    # Swap the given node value
    def swapData(self, a, b) :
        temp = a.data
        a.data = b.data
        b.data = temp
    # Sort the linked list using selection sort
    def selectionSort(self) :
        auxiliary = self.head 
        temp = None
        node = None
        # Execute linked list node
        while (auxiliary != None) :
            node = auxiliary
            temp = auxiliary.next
            # Find the minimum node
            while (temp != None) :              # min element node is pointed by node
                if (node.data > temp.data) :
                    node = temp
                # Visit to next node
                temp = temp.next

            if (auxiliary.data > node.data) :    #auxillary denotes the sorted subarray
                # Transfer minimum value to initial position
                # Swap the node value
                self.swapData(auxiliary, node)
            # Visit to next node
            auxiliary = auxiliary.next
    def main() :
        sll = SingleLL()
        # Constructed linked list
        # 2 → 5 → 0 → 8 → 2 → 4 → 9 → 7 → 0 → 1 → NULL
        sll.addNode(2)
        sll.addNode(5) 
        sll.addNode(0)
        sll.addNode(8)
        sll.addNode(2)
        sll.addNode(4)
        sll.addNode(9)
        sll.addNode(7)
        sll.addNode(0)
        sll.addNode(1)
        print("\n Before sort")
        sll.display()
        # Sort linked list
        sll.selectionSort()
        # 0 → 0 → 1 → 2 → 2 → 4 → 5 → 7 → 8 → 9 → NULL
        print("\n After sort")
        sll.display()
    

if __name__=="__main__":
    SingleLL.main()