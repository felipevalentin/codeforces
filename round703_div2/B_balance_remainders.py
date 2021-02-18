for i in range(int(input())):
    n = input()
    l = []
    ans = 0
    x = int(n) / 3
    for j in input().split():
        l += [int(j)%3]
    a = l.count(0)
    b = l.count(1)
    c = l.count(2)
    while a < x:
        ans += 1
        a += 1
        c -= 1
    while c < x:
        ans += 1
        c += 1
        b -= 1
    while b < x:
        ans += 1
        b += 1
        a -= 1
    while a < x:
        ans += 1
        a += 1
        c -= 1
    print(ans)