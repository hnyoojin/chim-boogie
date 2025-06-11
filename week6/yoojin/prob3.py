n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# 최대 보물 개수
max_treasure = [[0] * 3 for _ in range(n)]

# 젤 첫 층
max_treasure[0][0] = l[0]
max_treasure[0][1] = m[0]
max_treasure[0][2] = r[0]


for i in range(1, n):
    # Left : max(직전 Mid, 직전 Right)
    max_treasure[i][0] = \
        max(max_treasure[i-1][1], max_treasure[i-1][2]) + l[i]

    # Mid : max(직전 Left, 직전 Right)
    max_treasure[i][1] = \
        max(max_treasure[i-1][0], max_treasure[i-1][2]) + m[i]
        
    # Right : max(직전 Left, 직전 Mid)
    max_treasure[i][2] = \
        max(max_treasure[i-1][0], max_treasure[i-1][1]) + r[i]

print(max(max_treasure[n-1]))