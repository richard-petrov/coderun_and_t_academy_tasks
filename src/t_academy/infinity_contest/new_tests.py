import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    
    list_list = []

    for i in range(1, 10):
        while True:
            
            if i > m:
                break
            list_list.append(i)
            i = int(str(i) + str(i))
            print(i)

    list_list = [i for i in list_list if i >= n]

    print(len(list_list))
    

if __name__ == '__main__':
    main()