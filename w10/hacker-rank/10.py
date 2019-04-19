if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = student_marks[query_name]
    n, sm = len(res), 0
    for i in res:
        sm += i
    res = sm/n
    print('%.2f' % res)