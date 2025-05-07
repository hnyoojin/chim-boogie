n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 마을마다 사람 수 저장하는 리스트
village=[]

di=[(-1,0),(1,0),(0,-1),(0,1)]


def dfs(loc):
    global cnt
    y,x = loc
    # 아직 방문하지 않은 사람이 있는 곳은 카운트+1
    if 0<=y<n and 0<=x<n and grid[y][x] ==1:
        grid[y][x] = 2
        cnt+=1
        for dloc in di:
            dy, dx = dloc
            dfs((y+dy,x+dx))

# 배열 전체를 순회하며 dfs 호출
cnt=0
for i in range (n):
    for j in range(n):
        cnt=0
        dfs((i,j))
        # 처음 방문한 사람수가 1명 이상(마을)이면 village[]에 해당 마을의 사람 수 추가
        if cnt>0:
            village.append(cnt)

# 마을의 사람 수 오름차순 정렬
village.sort()

print (len(village))
print (*village,sep="\n")
