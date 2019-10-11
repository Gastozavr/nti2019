def C(n,k):
    if k == 0: 
        return 1
    if k == 1:
        return n
    if k > n/2:
        return C(n, n-k)
    return C(n-1, k-1) + C(n-1, k)

n = int(input())
for i in range(n+1):
    row = ""
    for k in range(i+1):
        row += "\t"+str(C(i,k))
    print(row)

