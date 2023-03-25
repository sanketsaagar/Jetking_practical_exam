
def splitevenodd(A):
    oddlist= []
    evenlist = []

    for i in A:
        if(i%2 ==0):
            evenlist.append(i)
        
        else:
            oddlist.append(i)
        
        print("The odd numbers are :", oddlist)
        print("The even numbers are :", evenlist)

A = list()
n = int(input(print("Enter size of list ")))
print("Enter the elements")
for i in range (int(n)):
    k = int(input(""))
    A.append(k)
splitevenodd(A)