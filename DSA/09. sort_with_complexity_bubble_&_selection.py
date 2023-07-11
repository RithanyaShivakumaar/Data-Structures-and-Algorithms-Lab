import random as rand
n1=0
n2=0
n3=0
n4=0
w=int(input("Enter the no. of executions"))
for i in range(0,w):
    a=[]
    n=int(input("Enter the no. of values to be entered"))
    for i in range(0,n):
        a.append(rand.randint(0,100))
    b=a
    c=a
    d=a 
    print("The Unsorted array") 
    print(a)
#Selection sort
    k1=0
    for i in range(0,n):
        x=i
        for j in range(i+1,n):
            if(a[x]>a[j]):
                x=j
            k1+=1
        a[x],a[i]=a[i],a[x]
        print("End of",i+1,"pass",a)
        k1+=1
    print("\nThe Ascending Sorted array using Selection sort")
    print(a)
    n1+=k1/n
    print("Complexity is ",k1/n)
    k1=0
    for i in range(0,n):
        x=i
        for j in range(i+1,n):
            if(b[x]<b[j]):
                x=j
            k1+=1
        b[x],b[i]=b[i],b[x]
        print("End of",i+1,"pass",b)
        k1+=1
    print("\nThe Descending Sorted array using Selection sort")
    print(b)
    n2+=k1/n
    print("Complexity is ",k1/n)
    k1=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(c[j]>c[j+1]):
                c[j],c[j+1]=c[j+1],c[j]
            k1+=1
        k1+=1
    print("\nThe Ascending Sorted array using Bubble sort")
    print(c)
    n3+=k1/n
    print("Complexity is ",k1/n)
    k1=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(d[j]<d[j+1]):
                d[j],d[j+1]=d[j+1],d[j]
            k1+=1
        k1+=1
    print("\nThe Descending Sorted array using Bubble sort")
    print(d)
    n4+=k1/n
    print("Complexity is ",k1/n)
print("Average Complexity of Selection sort in ascending is ",n1/w)
print("Average Complexity of Selection sort in descending is ",n2/w)
print("Average Complexity is Bubble sort in ascending is",n3/w)
print("Average Complexity is bubble sort in descending is ",n4/w)