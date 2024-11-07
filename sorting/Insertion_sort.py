def InsertionSort(a,n):
    for i in range(n):
        j=i
        while j>0 and a[j-1]>a[j]:
            t=a[j-1]
            a[j-1]=a[j]
            a[j]=t
            j-=1
    return a

arr=list(map(int,input().split()))
n=len(arr)
p=InsertionSort(arr,n)
print(p)