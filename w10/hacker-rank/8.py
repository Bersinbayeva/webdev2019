if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr = sorted(arr)
    print(arr[-2])