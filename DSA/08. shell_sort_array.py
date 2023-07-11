size =int(input("Enter size of the Array : "))
a=[]

for i in range(0,size):
    p=int(input(f"Enter Element {i+1} :"))
    a.append(p)
print("Before Sorting : ")
print(a)

k=len(a)//2

for i in range(0,k):
    for j in range(i,k):
        if a[j+k] < a[j]:
            a[j],a[j+k] = a[j+k],a[j]
    k=k//2   #divide the list until you reach the number one
    if k==1: #if reached one, come out of the loop and perform insertion osrt
        break

print("After shell sort : ",a)

if k==1: #normal insertion sort at last
        for i in range(1, len(a)):
            key = a[i]
            print(key)
            j = i-1
            while j >=0 and key < a[j] : 
                a[j+1] = a[j]
                j -= 1
                a[j+1] = key
print("After Sorting : ")
print(a) 