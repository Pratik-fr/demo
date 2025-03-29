def bubble(arr):
    n=len(arr)
    for passes in range(0,n):
        for i in range(0,n-1-passes):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

array=[5,4,3,2,1]
run=bubble(array)
print(run)        