
def BubbleSort(a,n):
    swap=0
    c=0  # NO OF TIMES OUTER LOOP WILL BE EXECUTED
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                swap+=1
        if swap==0:
            break
        c+=1
    print(c)
    return a

arr=list(map(int,input().split()))
n=len(arr)
p=BubbleSort(arr,n)
print(p)