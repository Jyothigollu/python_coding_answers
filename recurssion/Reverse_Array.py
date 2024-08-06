def reverse_arr(i,n,arr):
    #print(id(arr))
    if i>=n//2:
        return 
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i] 
    return reverse_arr(i+1,n,arr)
a=[1,2,3,4,5]
n=len(a)
reverse_arr(0,n,a)
#print(id(a))
print(a)