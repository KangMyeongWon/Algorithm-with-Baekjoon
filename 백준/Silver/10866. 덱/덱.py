import sys
from collections import deque

N = int(input())
queue = deque()

for i in range(N):
    in_cmd = sys.stdin.readline().split()

    if in_cmd[0] == "push_front":
        queue.appendleft(in_cmd[1])
    elif in_cmd[0] == "push_back":
        queue.append(in_cmd[1])
    elif in_cmd[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif in_cmd[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print("-1")
    elif in_cmd[0] == "size":
        print(len(queue))
    elif in_cmd[0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    elif in_cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print("-1")
    elif in_cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print("-1")