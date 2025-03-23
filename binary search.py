def binary(arr,target):
    size=len(arr)
    start=0
    end=size-1
    while(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end=mid-1
        elif(arr[mid<target]):
            start=mid+1
    return-1
array=[10,30,40,50,66,78,99,101]
target=99
run=binary(array,target)
print(run)