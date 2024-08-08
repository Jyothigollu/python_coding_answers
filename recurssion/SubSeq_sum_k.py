# INPUT l=[1,2,3] k=3
"""OUTPUT [1,2]
          [3]"""

def SubArrays(l,n,p,i,s,k):
    if n==i:
        if s==k:
            print(p)
        return 
    p.append(l[i])
    s+=l[i]
    SubArrays(l,n,p,i+1,s,k)
    s-=l[i]
    p.remove(l[i])
    SubArrays(l,n,p,i+1,s,k)
l=[1,2,1]
n=len(l)
p=[]
k=2
SubArrays(l,n,p,0,0,k)