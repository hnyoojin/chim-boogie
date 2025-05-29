# 입력
N = int(input())

def count_bst(n):
    # dp : 노드가 i개 있을때 만들 수 있는 BST 개수
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i):
            # Left (dp[j]), Right (dp[i-1-j]) 경우의수 더해서 전채 개수 구함
            dp[i] += dp[j] * dp[i - 1 - j]
    
    return dp[n]

print(count_bst(N))
