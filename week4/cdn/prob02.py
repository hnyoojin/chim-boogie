# BFS (너비 우선 탐색)을 이용하여 상한 귤이 다른 귤로 전염되는 시간을 계산하는 문제 !

from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 상한 시간 저장용 배열 (-1로 초기화)
time = [[-1] * n for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2: # 만약 처음부터 상한 귤이라면 
            queue.append((i, j)) # 큐에 삽입
            time[i][j] = 0  # 처음부터 상한 귤의 시간은 0

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행
while queue:
    x, y = queue.popleft() # 큐에서 상한 귤의 좌표를 꺼냄 time[x][y]
    for dir in range(4):   # 4방향 탐색 진행 
        nx = x + dx[dir]   
        ny = y + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and time[nx][ny] == -1: # 멀쩡한 귤 grid= 1이고 아직 방문 안 한 time = -1 라면
                time[nx][ny] = time[x][y] + 1 # time = 0
                queue.append((nx, ny))        # 해당 귤을 상하게 만듦 (큐에 넣음)

for i in range(n):
    row = []
    for j in range(n):
        if grid[i][j] == 0: # 비어 있으면 -1
            row.append(-1)
        elif grid[i][j] == 1: # 귤인데 감염되지 못하면 -2
            if time[i][j] == -1:
                row.append(-2)  
            else: # 귤인데 감염되면 time
                row.append(time[i][j])
        elif grid[i][j] == 2: # 처음부터 상했으면 0
            row.append(0)
    print(' '.join(map(str, row))) # 결과 출력
