n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
res = s1^s2
print(len(res))