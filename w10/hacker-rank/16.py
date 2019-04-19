n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    st = input().split()
    a = set(map(int, input().split()))
    if st[0]=='intersection_update':
        s = s&a
    elif st[0]=='update':
        s = s|a
    elif st[0]=='symmetric_difference_update':
        s = s^a
    elif st[0]=='difference_update':
        s = s-a
sm = 0
for i in s:
    sm += i
print(sm)