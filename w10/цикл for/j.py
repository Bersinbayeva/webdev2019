import sys
s = 0
for line in sys.stdin:
	for i in line.split():
		s += int(i)
print(s)