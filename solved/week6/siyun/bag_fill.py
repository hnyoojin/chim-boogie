N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [[0] * (M + 1) for _ in range(N + 1)]
# dp[i][w] = i는 현재까지 선택한 물건 갯수, 배낭 용량이 w일 때의 최대 가치

for i in range(1, N + 1): 
    for j in range(M + 1):  # 배낭 용량
        if j < w[i - 1]:  # 현재 물건 못 넣는 경우
            dp[i][j] = dp[i - 1][j]
        else:  # 현재 물건 넣을 수 있는 경우
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])

            
print(dp[N][M])
