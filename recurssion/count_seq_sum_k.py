# INPUT l=[1,2,3] k=3
"""OUTPUT [1,2]
          [3]
          c=2 """

def SubArrays(l,n,p,i,s,k):
    if n==i:
        if s==k:
            return 1
        return 0
    p.append(l[i])
    s+=l[i]
    f=SubArrays(l,n,p,i+1,s,k)
    s-=l[i]
    p.remove(l[i])
    r=SubArrays(l,n,p,i+1,s,k)
    return f+r
l=[1,2,1]
n=len(l)
p=[]
k=2
print(SubArrays(l,n,p,0,0,k))