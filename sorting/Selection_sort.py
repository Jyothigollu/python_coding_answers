def SelectionSort(a,n):
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if a[i]>a[j]:
                min=j 
        t=a[min]
        a[min]=a[i]
        a[i]=t
    return a

arr=list(map(int,input().split()))
n=len(arr)
p=SelectionSort(arr,n)
print(p)