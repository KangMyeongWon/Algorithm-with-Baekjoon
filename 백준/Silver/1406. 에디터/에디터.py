# array = list(input())
# cursor = len(array)
#
# for _ in range(int(input())):
#     do = list(input().split())
#     if do[0] == 'P':
#         array.insert(cursor, do[1])
#         cursor += 1
#     elif do[0] == 'L' and cursor > 0:
#             cursor -= 1
#     elif do[0] == 'D' and cursor < len(array):
#             cursor += 1
#     elif do[0] == 'B' and cursor > 0:
#             array.remove(array[cursor-1])
# print(*array)
##########################################################
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
# st1.extend(reversed(st2))
# print(*st1)
