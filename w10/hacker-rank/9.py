from decimal import Decimal
if __name__ == '__main__':
    mn, ss = set(), []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mn.add(score)
        ss.append([name, score])
    ss.sort()
    mn = sorted(mn)
    mn = mn[1]
    res = ''
    for i in ss:
        if i[1]== Decimal(mn):
            res += i[0] + '\n'
    print(res)