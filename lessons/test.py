def vosh(n, m):
    if n > m:
        return
    vosh(n+1, m)
    print(n*n)

vosh(1, 5)
print("====")
def nish(n):
    print(n*n)
    if n <= 1:
        return
    nish(n-1)

#nish(7)