# 기울어진 직사각형
# apr 10 : 1h
# apr 11 : 3h+..

# input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# def
def find_max_tilted_rectangle(n, grid):
    max_sum = 0
    
    # 모든 시작점
    for i in range(n):
        for j in range(n):
            # 직사각형 크기
            for h in range(1, n):
                for w in range(1, n):
                    # 직사각형이 격자 내부에 있는지 확인
                    if is_valid_rectangle(i, j, h, w, n):
                        current_sum = calculate_rectangle_sum(i, j, h, w, grid)
                        max_sum = max(max_sum, current_sum)
    
    return max_sum

# 기울어진 직사각형이 격자 내부에 있는지 확인
def is_valid_rectangle(i, j, h, w, n):
    # RU
    for k in range(1, h + 1):
        ni, nj = i + h + w - k, j - h + w + k
        if not (0 <= ni < n and 0 <= nj < n):
            return False
    # LU
    for k in range(1, w):
        ni, nj = i + w - k, j + w - k
        if not (0 <= ni < n and 0 <= nj < n):
            return False
    # LD
    for k in range(1, h + 1):
        ni, nj = i + k, j - k
        if not (0 <= ni < n and 0 <= nj < n):
            return False
    # RD
    for k in range(1, w + 1):
        ni, nj = i + h + k, j - h + k
        if not (0 <= ni < n and 0 <= nj < n):
            return False
    
    
    
    return True

# 기울어진 직사각형의 합
def calculate_rectangle_sum(i, j, h, w, grid):
    # 시작점
    total_sum = grid[i][j]
    
    # LD
    for k in range(1, h + 1):
        total_sum += grid[i + k][j - k]
    
    # RD
    for k in range(1, w + 1):
        total_sum += grid[i + h + k][j - h + k]
    
    # RU
    for k in range(1, h + 1):
        total_sum += grid[i + h + w - k][j - h + w + k]
    
    # LU
    for k in range(1, w):
        total_sum += grid[i + w - k][j + w - k]
    
    return total_sum


# print result
print(find_max_tilted_rectangle(n, grid))


'''
저는 시작지점을 00에서부터 n-1 n-1까지 순회시키면서,
각각 시작지점에 대해 LD -> RD -> RU -> LU 순서로 격자를 움직이도록 했습니다.

기울어진 사각형이라면 어느 방향으로, 어디서부터 순회하든 반드시 LD RD RU LU를 다 지나서 원점으로 돌아올거라 생각했음! (내가 맞음 아마도)

그래서 일단 LD RD RU LU를 False로 주고, global 설정을 해서, 각각 LD RD RU LU 함수를 통과하면 True가 되도록 했음!

------------------------------------------------------------------------------------------------------------

코드 수정했어요
함수명 변수명 좀 고치고,,,,,
코드를 수정했는데, 함수 이름과 변수명을 좀 더 직관적으로 바꿨어요!
h, w로 가능한 모든 기울어진 직사각형을 확인하는... 쪽으로..
'''