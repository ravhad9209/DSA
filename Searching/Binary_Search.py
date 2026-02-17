def binarySearch(arr,targetVal):
    start = 0 
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            start = mid + 1 
        else:
            end = mid - 1

    return -1

mylist = [3,4,5,1,2,9,7,8]
x = 3

new = binarySearch(mylist,x)

if new != -1:
    print("found at index",new) 

else :
    print("Not found")            