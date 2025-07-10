n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.

# i층에서 0=왼쪽, 1=가운대, 2=오른쪽을 선탹했을 때 
# 1층부터 i층까지 쫓겨나지 않고 모을 수 있는 보물의 최대 개수
dp = [[0] * 3 for _ in range(n)]

# 1층(인덱스 0)에서는 그냥 그 방의 보물 수만큼 가져갈 수 있다
dp[0][0] = l[0]
dp[0][1] = m[0]
dp[0][2] = r[0]

# 2층부터 n층까지 차례로 채워 나간다
for i in range(1, n):
    # i층에서 왼쪽 방 선택 → 이전 층에서는 가운데 or 오른쪽만 가능
    dp[i][0] = l[i] + max(dp[i-1][1], dp[i-1][2])
    # i층에서 가운데 방 선택 → 이전 층에서는 왼쪽 or 오른쪽만 가능
    dp[i][1] = m[i] + max(dp[i-1][0], dp[i-1][2])
    # i층에서 오른쪽 방 선택 → 이전 층에서는 왼쪽 or 가운데만 가능
    dp[i][2] = r[i] + max(dp[i-1][0], dp[i-1][1])

# 마지막 층(n-1)에서 세 방 중 가장 많은 보물을 가져간 경우가 정답
print(max(dp[n-1]))
