for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        h, l = max(a[i], a[i+1]), min(a[i], a[i+1])
        while l*2 < h:
            ans += 1
            l *= 2
    print(ans)