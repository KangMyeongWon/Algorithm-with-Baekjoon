import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            # 시작하는 칸을 큐에 넣기
            q.append((i, j))

# 큐에서 원소를 꺼내어(pop) 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            ans = -1
            print(ans)
            exit(0)
        ans = max(ans, board[i][j] -1 )

print(ans)