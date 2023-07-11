class Node :
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
    
def create(root) :
    while True :
        choice = int(input("1. Insert left 2. Insert right 0. Exit\nEnter choice : "))
        if root.data :
            if choice == 0 :
                break
            data = int(input("Enter data for the node : "))
            if data == root.data or data == root :
                continue
            elif choice == 1 :
                if root.left is None :
                    root.left = Node(data)
                    continue
                else :
                    root = root.left
                    root.left = Node(data)
            elif choice == 2 :
                if root.right is None :
                    root.right = Node(data)
                    continue
                else :
                    root = root.right
                    root.right = Node(data)
            else :
                print("Invalid Choice")
                return
        else :
            root = root.data

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

def insert(root, key):
    if root == None:
        temp = Node(key)
        return temp
 
    if key < root.data:
        root.left = insert(root.left, key)
 
    else:
        root.right = insert(root.right, key)
 
    return root

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
create(root)
while (True) :
    ele = int(input("\n1.Inorder \n2.Preorder \n3.Postorder \n4.Exit\nEnter your choice : "))

    if ele == 1 :
        inorder(root)
    
    if ele == 2 :
        preorder(root)

    if ele == 3 :
        ans = []
        postorder(root)
        print(ans)

    if ele == 4 :
        break
        
