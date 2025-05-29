from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 경로 탐색
def can_reach(min_val, max_val):
    if not (min_val <= grid[0][0] <= max_val):
        return False

    visited = [[False]*n for _ in range(n)]
    q = deque()
    q.append((0,0))
    # 시작점은 True로 바꿈
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return True

        # 이동 방향
        for dx, dy in [(1, 0), (0, 1)]:
            # 다음 칸 좌표
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if min_val <= grid[nx][ny] <= max_val:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return False

# diff 에 해당하는 경로 조사
def check(diff):
    for min_val in range(0, 101):
        max_val = min_val + diff
        if max_val > 100:
            break
        # 경로가 하나라도 있으면 True 반환
        if can_reach(min_val, max_val):
            return True
    return False

left, right = 0, 100
answer = 100

# diff 이진 탑색
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
