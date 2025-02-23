import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
answer = [-1]*N
stack = []

for i in range(N):
    while stack and array[stack[-1]] < array[i]:
        answer[stack[-1]] = array[i]
        stack.pop()
    stack.append(i)
print(*answer)