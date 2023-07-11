from array import *
from tkinter import END
a = array('i',[])

def insertion(a):
    val = int(input("\nEnter the value needed to be inserted : "))
    pos = int(input("Enter the position where in which it needs to be inserted : "))
    if (pos > size) :
        print("The index specified is out of range")
        END
    else :
        a.insert(pos,val)
        print(f"Element {val} is successfully inserted at position {pos} in the array")
        print(a)
   
def reversal(a):
    print("\nOriginal Array : ")
    print(a)
    print("Array Reversed : ")
    print(a[::-1])

def removal(a):
    rem=int(input("\nEnter the value that needs to be removed : ")) 
    flag = 0
    for x in range(0,n) :
        if a[x] == rem : 
            flag = 1    
            a.remove(rem)
            print(f"Element {rem} has successfully been removed from the array")
            print(a)
            break
    if flag != 1 :
        print(f"Element {rem} is not found in the Array")
        END
   
n=int(input("Enter size of array : "))
for x in range(0,n):
    print(f"Enter element {x} : ") # f is basically the format specifier, like %d in c
    ele=int(input())
    a.append(ele)

print(a)
size=len(a)
print("\n1. Insertion")
print("2. Reverse Traversal")
print("3. Deletion")
print("4. Exit")
new=int(input("Enter your choice : "))

while new!=4:
    if new==1:
        insertion(a)
        
    elif new==2:
        reversal(a)
        
    elif new==3:
        removal(a)
        
    elif new==4:
        print("\nEXIT")
        exit()
    else:
        print("Enter valid value")

    print("\n1. Insertion")
    print("2. Reverse Traversal")
    print("3. Deletion")
    print("4. Exit")
    new=int(input("Enter your choice : "))