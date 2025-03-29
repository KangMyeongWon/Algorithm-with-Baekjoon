import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    # 시작하는 칸을 큐에 넣고 방문했다는 표시(●)를 남김
    board[x][y] = 0
    dist[x][y] = 1
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 큐에서 원소를 꺼내어(pop) 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                board[nx][ny] = 0
                q.append((nx, ny))
    return dist[n-1][m-1]

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dist = [ [ 0 for _ in range(m) ] for _ in range(n)]

print(bfs(0,0))