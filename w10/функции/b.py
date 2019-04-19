def power(a, n):
	res = 1
	while n>0:
		res *= a
		n -= 1
	return res

inp = list(map(int, input().split()))
a, n = inp
print(power(a, n))