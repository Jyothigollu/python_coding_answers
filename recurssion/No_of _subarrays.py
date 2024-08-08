# INPUT l=[1,2,3]
"""OUTPUT [1,2,3]
          [1,2]
          [1,3]
          [1]
          [2,3]
          [2]
          [3]
          []"""

def SubArrays(l,n,p,i):
    if n==i:
        print(p)
        return 
    p.append(l[i])
    SubArrays(l,n,p,i+1)
    p.remove(l[i])
    SubArrays(l,n,p,i+1)
l=[1,2,3]
n=len(l)
p=[]
SubArrays(l,n,p,0)