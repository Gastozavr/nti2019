def C(n,k):
    if k == 0: 
        return 1
    if k == 1:
        return n
    if k > n/2:
        return C(n, n-k)
    return C(n-1, k-1) + C(n-1, k)

n = 10
s = 0
p = 1
for i in range(10,0,-1):
    s += C(n,i)**2
    #print(i,C(n,i))
print(s)
