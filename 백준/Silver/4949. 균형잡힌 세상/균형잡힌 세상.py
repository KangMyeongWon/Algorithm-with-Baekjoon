import sys
from collections import deque
input = sys.stdin.readline

while True:
    arr = input().rstrip()
    q = deque()
    if arr == ".":
        break
    for i in arr:
        if i in "([":
            q.append(i)
        elif i == ")":
            if q:
                if q[-1] == "(":
                    q.pop()
                else:
                    q.append(i)
                    break
            else:
                q.append(i)
                break
        elif i == "]":
            if q:
                if q[-1] == "[":
                    q.pop()
                else:
                    q.append(i)
                    break
            else:
                q.append(i)
                break
    if q:
        print("no")
    else:
        print("yes")