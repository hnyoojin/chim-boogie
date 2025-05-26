# DFS 기반 마을 찾기 코드 !
# 1은 사람 있는 칸 0은 벽, 상하좌우로 연결된 1들을 하나의 마을로 간주
# 총 마을 개수와, 각 마을에 있는 사람 수를 구하고 오름차순으로 출력하는 문제
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)] # 이미 방문한 좌표인지 여부 저장용 

# 방향 벡터: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1  # 현재 사람 포함
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny) # 하나의 마을 내 사람 수를 count로 합산해서 리턴 
    return count

village_sizes = []

# 격자 전체를 도는 이중 for문 
for i in range(n): 
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]: # 아직 방문하지 않은 사람을 만나면 
            village_sizes.append(dfs(i, j)) # dfs로 그 마을 전체를 방문하며 사람 수를 구함, 사람 수 리스트에 저장 

village_sizes.sort() # 사람 수를 오름차순으로 정렬 

# 출력
print(len(village_sizes))
for size in village_sizes:
    print(size)
