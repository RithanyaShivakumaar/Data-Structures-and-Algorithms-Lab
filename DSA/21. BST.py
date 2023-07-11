class Node :
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
    
    def create(self) :
        cnt = int(input("Enter the total number of nodes : "))
        for i in range(cnt) :
            data = int(input(f"Enter data for Node {i+1} : "))
            self.add(data)

    def add(self,data) :
        if self.data :
            if (data == self.data or data ==  root): #Takes care of duplication
                return
            elif data < self.data : #creates left subtree
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.add(data)
            elif data > self.data : #creates right subtree
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.add(data)
        else :
            self.data = data

def search(root,key) :
    while root != None : # traverse until root reaches dead end
        if key > root.data :  # check right subtree
            root = root.right  

        elif key < root.data : #check left subtree
            root = root.left

        else :
            return True
    return False

def delete(root, key):
    curr = root
    prev = None

    while(curr != None and curr.data != key): #check if key is present in tree, if present prev points to the parent tof the node to be deleted
        prev = curr
        if curr.data < key:
            curr = curr.right
        else:
            curr = curr.left
 
    if curr == None:
        print("The specified element is not present in the tree")
        return root
 
    # Check if the node to be deleted has atmost one child
    if curr.left == None or curr.right == None:
 
        # newCurr will replace the node to be deleted.
        newCurr = None
 
        # if the left child does not exist.
        if curr.left == None:
            newCurr = curr.right
        else:
            newCurr = curr.left
 
        # check if the node to be deleted is the root.
        if prev == None:
            return newCurr
 
        # Check if the node to be deleted is prev's left or right child and then replace this with newCurr
        if curr == prev.left:
            prev.left = newCurr
        else:
            prev.right = newCurr
 
        curr = None
    # node to be delete has two children.
    else:
        p = None
        temp = None
 
        # Compute the inorder successor of curr.
        temp = curr.right
        while temp.left is not None:
            p = temp
            temp = temp.left
        # check if the parent of the inorder successor is the root or not.
        # if it isn't, then make the left child of its parent equal to the inorder successor's right child.
        if p != None:
            p.left = temp.right
 
        else:
            # if the inorder successor was the root, then make the right child of the node to be deleted equal to the right child of the inorder successor.
            curr.right = temp.right
 
        curr.data = temp.data
        temp = None
 
    return root

def inorder(root) :
    curr = root
    stack = []
    while True :
        if curr is not None :  # reach the leftmost node of the current node
            stack.append(curr)
            curr = curr.left
        elif (stack) :  # backtrack from the empty subtree and visit the node at the top of the stack
            curr = stack.pop()
            print(curr.data, end = " ")
            curr = curr.right  #left subtree is done, now right subtree
        else : 
            break

def preorder(root) :
    if root is None :
        return
    stack = []
    stack.append(root) #NLR, push root in first
    ''' Procedure :
    1. Print 2. Push its right child 3. Push its left child
    Right child is pushed before, as left child can be accessed first
    '''
    while (stack) :
        node = stack.pop() # pop and print the item
        print(node.data, end = " ")
        if node.right is not None :
            stack.append(node.right)
        if node.left is not None :
            stack.append(node.left)

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def insert(root, key):  #insert a node iteratively into the tree
    new = Node(key)
    ptr = root
    par = None
    while ptr is not None :
        par = ptr
        if ptr.data == key :  #takes care of duplication
            print("The element is already present in the tree. Thus cannot be inserted")
            return
        elif key < ptr.data :
            ptr = ptr.left
        elif key > ptr.data :
            ptr = ptr.right
    if par == None :
        par = new
    elif key < par.data :
        par.left = new
    elif key > par.data :
        par.right = new
    return par

def postorder(root):
         
    if root is None: # Check for empty tree
        return
    stack = []
    while(True):
         
        while (root):
            if root.right is not None:  # Push root's right child and then root to stack
                stack.append(root.right)
            stack.append(root)
            root = root.left  # Set root as root's left child
         
        root = stack.pop() # Pop an item from stack and set it as root
 
        # If the popped item has a right child and the right child is not processed yet, then make sure right child is processed before root
        if (root.right is not None and
            peek(stack) == root.right):
            stack.pop() # Remove right child from stack
            stack.append(root) # Push root back to stack
            root = root.right # change root so that the right child is processed next
 
        else:   # Else print root's data and set root as None
            ans.append(root.data)
            root = None
 
        if (len(stack) <= 0):
                break
root = Node(int(input("Enter root Node : ")))
root.create()
while (True) :
    ele = int(input("\n1.Search \n2.Delete a node \n3.Inorder \n4.Preorder \n5.Postorder \n6.Insert a node \n7.Exit\nEnter your choice : "))
    if ele == 1 :
        key = int(input("Enter the element to be searched in the tree : "))
        if search(root,key) :
            print("The element is present")
        else :
            print("The element is not present")

    if ele == 2 :
        dell = int(input("Enter the element to be deleted : "))
        delete(root,dell)
        print(f"\nAfter deleting {dell} from tree : ")
        inorder(root)

    if ele == 3 :
        inorder(root)
    
    if ele == 4 :
        preorder(root)

    if ele == 5 :
        ans = []
        postorder(root)
        print(ans)

    if ele == 6 :
        val = int(input("Enter the value to insert : "))
        insert(root,val)
        inorder(root)

    if ele == 7 :
        break
        
