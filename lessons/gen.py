def f(s, t, n, k):
    if t == n:
        print(s)
        return
    for i in range(1, k+1):
        f(s + " " + str(i), t + 1, n, k)

n, k = map(int, input().split())
f("", 0, n, k)