n = int(input())
ok = True
while n!=1:
	if n%2==1:
		ok = False
		break
	n /= 2
if ok==False:
	print('NO')
else:
	print('YES')