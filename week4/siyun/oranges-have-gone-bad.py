from collections import deque 
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans=[[-1 for _ in range(n)]for _ in range (n)]
queue=deque()
di=[(1,0),(-1,0),(0,1),(0,-1)]

# 상하는데 걸린 시간 갱신 및 큐에 넣기
def push(loc,cnt):
    y,x = loc
    ans[y][x]=cnt
    queue.append(loc)


def bfs():
    while queue:
        loc=queue.popleft()
        for dloc in di:
            y,x = loc
            dy, dx = dloc
            cnt=ans[y][x]
            y+=dy
            x+=dx
            # 방문한 적 없으면서 안상한 귤은 push()
            if 0<=y<n and 0<=x<n and grid[y][x]==1 and ans[y][x]==-1:
                push((y,x),cnt+1)

    # 끝까지 상하지 않은 귤은 -2
    for i in range (n):
        for j in range (n):
            if grid[i][j]==1 and ans[i][j]==-1 : 
                ans[i][j]=-2

# 상한 귤 위치 찾아서 큐에 넣어 초기화
def find_spoiled_loc():
    for i in range (n):
        for j in range (n):
            if grid[i][j]==2:
                push((i,j),0)

find_spoiled_loc()
bfs()

# 결과 출력
for row in ans:
    print (*row)
