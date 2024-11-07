def Merge(a,low,mid,high):
    t=[]
    left=low
    right=mid+1
    while left<=mid and right<=high :
        if a[left]<a[right]:
            t.append(a[left])
            left+=1
        else:
            t.append(a[right])
            right+=1
    while left<=mid:
        t.append(a[left])
        left+=1
    while right<=high:
        t.append(a[right])
        right+=1
    for i in range(low,high+1):
        a[i]=t[i-low]
def MergeSort(a,low,high):
    if low==high:
        return
    mid=(low+high)//2
    MergeSort(a,low,mid)
    MergeSort(a,mid+1,high)
    Merge(a,low,mid,high)
    return a

arr=list(map(int,input().split()))
low=0
high=len(arr)-1
p=MergeSort(arr,low,high)
print(p)