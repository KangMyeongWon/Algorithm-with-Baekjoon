import sys
from array import array

N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    key_input = list(sys.stdin.readline().split())

    if key_input[0] == "push":
        array.insert(len(array), key_input[1])
    elif key_input[0] == "pop":
        if len(array) == 0:
            print('-1')
        else:
            print(array.pop())
    elif key_input[0] == "size":
        print(len(array))
    elif key_input[0] == "empty":
        if len(array) == 0:
            print('1')
        else:
            print('0')
    elif key_input[0] == "top":
        if len(array) == 0:
            print('-1')
        else:
            print(array[len(array) - 1])