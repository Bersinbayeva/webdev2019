k = int(input())
l = list(map(int, input().split()))
l.sort()
i = 0
while i<len(l):
    if i==len(l)-1:
        print(l[i])
        break
    elif l[i]==l[i+1]:
        i += k
    else:
        print(l[i])
        break