# tail recurssion
"""def sum_Numbers(N,s):
    if N==0:
        return s
    return sum_Numbers(N-1,s+N)
n=int(input())
print(sum_Numbers(n,0))"""


#head recurrsion
def head_recursive_sum(N):
    if N == 0:
        return 0
    temp_sum = head_recursive_sum(N-1)  # Recursive call is not the last operation
    return temp_sum + N  # Operation after the recursive call

n = int(input("Enter a number: "))
print(head_recursive_sum(n))

