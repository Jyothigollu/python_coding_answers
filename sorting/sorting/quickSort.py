def Partition(a,low,high):
    pivot=a[low]
    i=low
    j=high
    while i<j:
        while a[i]<=pivot and i<high:
            i+=1
        while a[j]>pivot and j>low:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[low],a[j]=a[j],a[low]
    return j
def QuickSort(a,low,high):
    if low<high:
        p=Partition(a,low,high)
        QuickSort(a,low,p-1)
        QuickSort(a,p+1,high)
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
QuickSort(arr,low,high)
print(arr)