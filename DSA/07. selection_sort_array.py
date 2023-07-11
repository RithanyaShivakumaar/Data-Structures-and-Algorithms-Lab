a = []
size = int(input("Enter the size : "))
for i in range(size) :
    data = int(input(f"Enter Element {i+1} : "))
    a.append(data)

print("Array Before Sorting : ")
print(a)

for i in range(0,size) :
    min  = i
    for j in range(i+1,size) :
        if a[j] < a[min] :
            min = j
    (a[i], a[min]) = (a[min], a[i])         #good way of swapping
    

print("Array after sorting : ")
print(a)


