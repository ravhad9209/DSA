def buubleSort(a):
    size = len(a)

    for j in range(size):
        isSwapped = False
        for j in range(0,size-j-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                isSwapped = True  

        if (isSwapped == False):  
            break  


def printArray(a):
    for i in a:
        print(i,end=" ")
    print("")

a = [10,4,9,7,2,15]

print("Before Swap :")
printArray(a)

buubleSort(a)

print("After Swap :")

printArray(a)