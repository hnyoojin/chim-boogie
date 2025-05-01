# 실패! ㅎㅎ..
n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

def max_value_stolen(N, M, C, weights):
    best_options = []
    
    for r in range(N):
        options = []
        for c in range(N - M + 1):
            items = weights[r][c:c+M]
            
            values = [w*w for w in items]
            max_value = knapsack(items, values, C)
            
            options.append((max_value, c, c+M-1))
        
        best_options.append(options)
    
    max_total_value = 0
    
    for r1 in range(N):
        for i, (val1, start1, end1) in enumerate(best_options[r1]):
            for j, (val2, start2, end2) in enumerate(best_options[r1]):
                if i != j and (end1 < start2 or end2 < start1):
                    max_total_value = max(max_total_value, val1 + val2)
            
            for r2 in range(N):
                if r1 != r2:
                    for val2, _, _ in best_options[r2]:
                        max_total_value = max(max_total_value, val1 + val2)
    
    return max_total_value

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    
    return dp[capacity]


print(max_value_stolen(N, M, C, weights))
