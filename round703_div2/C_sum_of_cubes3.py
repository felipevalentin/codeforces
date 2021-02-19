for t in range(int(input())):
    n = int(input())
    ans = "NO"
    i = 1
    while i**3 < n:
        j = round(((n-i**3)**(1/3)))
        if i**3 + j**3 == n:
            ans = "YES"
        i += 1
    print(ans)