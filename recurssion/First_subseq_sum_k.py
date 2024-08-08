"""
Input : [1,2,1]
output :[1,1]
"""
def SubArrays(l,n,p,i,s,k):
    if n==i:
        if s==k:
            return True
        return 
    p.append(l[i])
    s+=l[i]
    if(SubArrays(l,n,p,i+1,s,k)):
        return True
    s-=l[i]
    p.remove(l[i])
    if(SubArrays(l,n,p,i+1,s,k)):
        return True
l=[1,2,1]
n=len(l)
p=[]
k=2
if(SubArrays(l,n,p,0,0,k)):
    print(p)