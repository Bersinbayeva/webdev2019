t = int(input())
for i in range(t):
    n1 = int(input())
    s1 = set(map(int, input().split()))
    n2 = int(input())
    s2 = set(map(int, input().split()))
    if s2==s1|s2:
        print('True')
    else:
        print('False')