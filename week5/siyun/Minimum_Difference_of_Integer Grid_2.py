import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# dp는 최대값만 저장
INT_MAX=sys.maxsize
MAX_R= 100
dp=[[[0] for _ in range(n)]for _ in range (n)]

def init():
    # dp (0,0) 기준 행, 열은 미리 값 세팅
    dp[0][0]=grid[0][0]
    for i in range (1,n):
        dp[0][i]=max(dp[0][i-1],grid[0][i])
        dp[i][0]=max(dp[i-1][0],grid[i][0])
        
# lower_bound 미만인 모든 셀을 지나갈 수 없는 벽으로 만든다
def solve(lower_bound):
    for i in range (n):
        for j in range (n):
            if grid[i][j]<lower_bound:
                grid[i][j]=INT_MAX

    #dp값 업데이트
    init()
    for i in range (1,n):
        for j in range (1,n):
            # dp의 값 = 해당 위치의 왼쪽 혹은 위쪽 수를 선택했을 때 최대-최소값이 작게 되는 값 선택
            dp[i][j]=max(min(dp[i][j-1],dp[i-1][j]),grid[i][j])

    # 도착지까지 가는 경로의 최대값 반환
    return dp[n-1][n-1]

ans=INT_MAX
# 1~100까지의 lower_bound를 적용해 최대-최소값 풀이
for i in range (1,MAX_R+1):
    upper_bound = solve(i)
    if upper_bound==INT_MAX:
        continue
    # 최대-최소값이 더 작은 값으로 갱신
    ans=min(upper_bound-i,ans)

print(ans)
