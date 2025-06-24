import sys


def main():

    list_ = []
    counter = 0

    for i in map(int, input().split()):
        list_.append(i)
    
    for i in range(1, len(list_) - 1):
        if list_[i] > list_[i - 1] and list_[i] > list_[i + 1]:
            counter += 1

    print(counter)

if __name__ == '__main__':
    main()