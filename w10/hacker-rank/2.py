N = int(input())
if N%2==1:
    print('Weird')
elif N%2==0 and N in range(6, 21):
    print('Weird')
else:
    print('Not Weird')