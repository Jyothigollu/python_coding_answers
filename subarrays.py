
# time complixity O(n^3)
"""def generate_sublists(l, start=0, current=[]):
    if start == len(l):
        return
    current = current + [l[start]]
    print(current)
    generate_sublists(l, start + 1, current)

def recursive_sublists(l):
    for s in range(len(l)):
        generate_sublists(l, s)"""

# time complixity O(n^2)

l=[1,2,3,4]
for s in range(len(l)):
    p=[]
    for e in range(s,len(l)):
        p+=[l[e]]
        print(p)

