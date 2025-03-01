import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline().strip())

for _ in range(N):
    array = list(sys.stdin.readline().strip().split())
    if array[0] == 'push':
        queue.append(array[1])
    elif array[0] == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.popleft())
    elif array[0] == 'size':
        print(len(queue))
    elif array[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif array[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])