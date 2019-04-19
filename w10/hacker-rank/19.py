s = set(map(int, input().split()))
n = int(input())
ok = True
for i in range(n):
    s1 = set(map(int, input().split()))
    if s!=s|s1:
        ok = False
        print(ok)
        break
if ok==True:
    print(ok)