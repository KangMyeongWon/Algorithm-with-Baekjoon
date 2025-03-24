import sys
from collections import deque
input = sys.stdin.readline

num_cmd = int(input())
for _ in range(num_cmd):
    cmd = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    reverse_num = 0
    error_flag = False
    for i in cmd:
        if i == "R":
            reverse_num += 1
        elif i == "D":
            if arr:
                if reverse_num %2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                error_flag = True
                break
                
    if not error_flag:
        if reverse_num % 2 == 1:
            arr.reverse()
        print("["+",".join(arr)+"]")