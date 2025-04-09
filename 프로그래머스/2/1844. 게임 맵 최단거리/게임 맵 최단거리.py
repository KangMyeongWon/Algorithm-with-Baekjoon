from collections import deque
import ast

def solution(maps):
    n = len(maps)  # 행
    m = len(maps[0])  # 열
    
    board = [[0] * m for _ in range(n)]

    answer = 0
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q.append((0,0))
    maps[0][0] = 0
    board[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny  = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    answer = board[-1][-1]
    if answer == 0:
        return -1
    else:
        return answer