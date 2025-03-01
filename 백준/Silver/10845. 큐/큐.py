import sys

N = int(sys.stdin.readline().strip())

answer = []

for i in range(N):
    array = list(sys.stdin.readline().strip().split())
    if array[0] == 'push':
        answer.append(array[1])
    elif array[0] == 'pop':
        if len(answer) == 0:
            print('-1')
        else:
            print(answer.pop(0))
    elif array[0] == 'size':
        print(len(answer))
    elif array[0] == 'empty':
        if len(answer) == 0:
            print('1')
        else:
            print('0')
    elif array[0] == 'front':
        if len(answer) == 0:
            print('-1')
        else:
            print(answer[0])
    else:
        if len(answer) == 0:
            print('-1')
        else:
            print(answer[len(answer) - 1])