#BEST SOLUTION BY FAR
a = set()
for i in range(1, 10001):
    a.add(i**3)
for i in range(int(input())):
    n = int(input())
    ans = "NO"
    for j in a:
        if n-j in a:
            ans = "YES"
    print(ans)