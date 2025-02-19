import sys

# 초기 문자열 입력
left_stack = list(sys.stdin.readline().strip())  # 커서 왼쪽 부분 (리스트)
right_stack = []  # 커서 오른쪽 부분 (스택)

# 명령어 개수 입력
n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == 'P':  # 문자 삽입
        left_stack.append(command[1])
    elif command[0] == 'L' and left_stack:  # 왼쪽 이동
        right_stack.append(left_stack.pop())
    elif command[0] == 'D' and right_stack:  # 오른쪽 이동
        left_stack.append(right_stack.pop())
    elif command[0] == 'B' and left_stack:  # 문자 삭제
        left_stack.pop()

# 최종 결과 출력 (왼쪽 + 오른쪽 역순)
print("".join(left_stack + right_stack[::-1]))