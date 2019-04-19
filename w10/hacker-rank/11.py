n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    st = input().split()
    if len(st)==1:
        s.pop()
    elif st[0]=='remove':
        s.discard(int(st[1]))
    else:
        s.discard(int(st[1]))
sm = 0
for i in s:
    sm += i
print(sm)