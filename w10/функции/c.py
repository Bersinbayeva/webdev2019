def xor(x, y):
	if x==y:
		return 0
	return 1
a = list(map(int, input().split()))
print(xor(a[0], a[1]))