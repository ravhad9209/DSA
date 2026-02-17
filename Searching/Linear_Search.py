def LinearSearch(arr,TargetVal):
    for i in range (len(arr)):
        if arr[i] == TargetVal:
            return i 
    return -1 
    
mylist = [12,64,23,98,75,15,32,15,46]
x = 15

new = LinearSearch(mylist,x)

if new != 1:
    print("found at index ",new)
 
else :
    print("not Found") 
