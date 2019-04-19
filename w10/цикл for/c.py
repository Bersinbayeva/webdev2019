a = int(input())
b = int(input())
for i in range(a, b+1):
	j = int(i**0.5)
	if j**2==i:
		print(i, end=' ')