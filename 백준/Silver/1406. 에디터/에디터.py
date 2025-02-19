import sys

left_s = list(sys.stdin.readline().strip())
right_s = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'P':
        left_s.append(command[1])
    elif command[0] == 'L' and left_s:
        right_s.append(left_s.pop())
    elif command[0] == 'D' and right_s:
        left_s.append(right_s.pop())
    elif command[0] == 'B' and left_s:
            left_s.pop()
print("".join(left_s + right_s[::-1]))