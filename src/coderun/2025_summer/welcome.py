def solution(n, m):
    min_, max_ = min(n, m), max(n, m)
    ostatok = max_ % min_
    counter = 0
    for i in range(1, min_ + 1):
        if (i ** 2 <= min_ * 2) and ((i % 2 == 0) or (i == 0)):
            print(counter)
            counter += 1
        elif (i ** 2 <= (min_ * 2 + ostatok)) and (i % 2 == 1):
            print(counter)
            counter += 1
        else:
            break
    return counter

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solution(n, m))

