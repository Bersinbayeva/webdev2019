if __name__ == '__main__':
    N = int(input())
    ls = []
    for i in range(N):
        s = input().split()
        if s[0]=='insert':
            ls.insert(int(s[1]), int(s[2]))
        elif s[0]=='print':
            print(ls)
        elif s[0]=='append':
            ls.append(int(s[1]))
        elif s[0]=='pop':
            ls.pop()
        elif s[0]=='sort':
            ls.sort()
        elif s[0]=='reverse':
            ls.reverse()
        elif s[0]=='remove':
            ls.remove(int(s[1]))