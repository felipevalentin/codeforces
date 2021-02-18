for i in range(int(input())):
    n = int(input())
    a = [-n//3]*3
    ans = 0
    for j in input().split():
        a[int(j)%3] += 1
    for j in range(-3, 2):
        if a[j] > 0:
            ans += a[j]
            a[j+1] += a[j]
            a[j] = 0
    print(ans)