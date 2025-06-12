N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.

# dp 테이블 초기화 
dp = [0] * (M + 1)

for i in range(N):
    weight_i = w[i]
    value_i = v[i]

    for j in range(M, weight_i - 1, -1):
        # “이 물건을 담았을 때” vs “담지 않았을 때” 중 큰 값을 선택
        candidate = dp[j - weight_i] + value_i
        if candidate > dp[j]:
            dp[j] = candidate
# 허용 무게를 최대치인 M으로 잡았을 때의 최대값
print(dp[M])
