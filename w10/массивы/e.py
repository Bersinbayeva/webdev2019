ok = False
n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
	if a[i]>=0 and a[i+1]>=0:
		ok = True
	elif a[i]<0 and a[i+1]<0:
		ok = True
if ok == True:
	print('YES')
else:
	print('NO')