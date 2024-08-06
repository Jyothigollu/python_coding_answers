def recurssion(i,n):
    if i==0:
        return
    print(i,n) # prints 5 to 1
    recurssion(i-1,n)
    print(i)  #prints 1 to 5
n=int(input())
recurssion(5,n)