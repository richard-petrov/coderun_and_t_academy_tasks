import sys


def main():
    workers_num, t = map(int, sys.stdin.readline().split())
    floors = list(map(int, sys.stdin.readline().split()))
    left_worker = int(sys.stdin.readline().strip())

    down_to_left = floors[:left_worker]
    up_to_left = floors[(left_worker - 1):]

    if (t >= down_to_left[-1] - down_to_left[0]) or (t >= up_to_left[-1] - up_to_left[0]):
        print(floors[-1] - floors[0])
    else:
        if down_to_left <= up_to_left:
            print((floors[left_worker - 1]) - floors[0] + floors[-1] - floors[0])
        elif up_to_left < down_to_left:
            print(floors[-1] - (floors[left_worker - 1]) + floors[-1] - floors[0])
    

if __name__ == '__main__':
    main()