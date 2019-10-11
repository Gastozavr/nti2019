def C(n,k):
    if k == 0: 
        return 1
    if k == 1:
        return n
    if k > n/2:
        return C(n, n-k)
    return C(n-1, k-1) + C(n-1, k)
print(C(10,3))

sum = 0
for i in range(2,10):
    for j in range(i+1,11):
        for k in range(j+1, 12):
            sum += 1
            print(sum, i, j, k)
print(C(9,2))
print(C(7,3))
print(C(10,3))
print(36*35*120)
s = C(9,2) * C(7,3) * C(10, 3) * 6
print(s)    