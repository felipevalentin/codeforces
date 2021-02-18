t = int(input())
for i in range(t):
    n = input()
    a = list(map(int, input().split()))
    x = 0
    ans = 0
    while x < len(a)-1:
        h = max(a[x], a[x+1])
        l = min(a[x], a[x+1])
        if h / l <= 2:
            x += 1
        else:
            a.insert(x+1, l*2)
            ans += 1
    print(ans)