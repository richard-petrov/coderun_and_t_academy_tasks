import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))

    numbers_str = [list(str(i)) for i in numbers]

    numbers_strip = []

    potential_gains = []

    for i in numbers_str:
        numbers_strip.append(list(map(int, i)))

    numbers_strip.sort(reverse=True)


    for i in numbers_strip:
        l = []
        for j in range(len(i)):
            potential_gains.append((9 * (10 ** (len(i) - j - 1))) - (i[j] * (10 ** (len(i) - j - 1))))
    potential_gains.sort(reverse=True)

    print(sum(potential_gains[:m]))

if __name__ == '__main__':
    main()