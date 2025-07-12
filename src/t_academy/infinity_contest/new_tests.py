import sys


def main():
    L, R = map(int, sys.stdin.readline().split())
    
    count = 0

    for digit in range(1, 10):
        current_num = digit

        while True:
            
            if L <= current_num <= R:
                count += 1
            if current_num > R:
                break
            if R // 10 < current_num:
                break

            current_num = current_num * 10 + digit

    print(count)
    

if __name__ == '__main__':
    main()