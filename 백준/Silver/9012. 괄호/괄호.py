import sys
from collections import deque
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    cmd = input().rstrip()
    queue = deque()
    flag = False

    for i in cmd:
        if i == '(':
            queue.append(i)
        else:
            if queue:
                queue.pop()
            else:
                flag = True
                break

    if flag or queue:
        print("NO")
    else:
        print("YES")