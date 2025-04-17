
# input
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# def

# 90도 회전 로직
def rotate_90(grid):
    return [list(row) for row in zip(*grid[::-1])]

# 중력 적용 로직
def apply_gravity(grid):
    # 열 순회
    for col in range(n):
        # 열에 남아있는 모든 폭탄만 뽑아서, 아래에서부터 차례대로 채우기
        column = [grid[row][col] for row in range(n) if grid[row][col] != 0]
        new_column = [0] * (n - len(column)) + column
        
        # grid에 중력 반영
        for row in range(n):
            grid[row][col] = new_column[row]
    
    return grid

# 폭탄 폭발 로직
def explode_bombs(grid):
    exploded = [[False] * n for _ in range(n)]
    is_exploded = False

    # 가로 방향 폭발 그룹 확인
    for i in range(n):
        j = 0
        while j < n:
            if grid[i][j] == 0:
                j += 1
                continue
            
            count = 1
            while j + count < n and grid[i][j] == grid[i][j+count]:
                count += 1
            
            if count >= m:
                is_exploded = True
                for k in range(j, j+count):
                    exploded[i][k] = True
            
            j += count

    # 세로 방향 폭발 그룹 확인
    for j in range(n):
        i = 0
        while i < n:
            # 빈칸 뛰어넘기
            if grid[i][j] == 0:
                i += 1
                continue
            
            # count를 1로 초기화
            count = 1

            # 격자를 벗어나지 않는 한에서, 동일한 수의 연속 횟수 체크
            while i + count < n and grid[i][j] == grid[i+count][j]:
                count += 1
            
            # m 이상이면 폭발
            if count >= m:
                is_exploded = True
                for k in range(i, i+count):
                    exploded[k][j] = True
            
            # 다음 그룹으로 이동
            i += count
    
    # 폭발한 폭탄 제거
    for i in range(n):
        for j in range(n):
            if exploded[i][j]:
                grid[i][j] = 0
    
    return grid, is_exploded

def solve_bomb_puzzle(grid, k):
    left_bomb = 0

    # 회전-폭발 K번 반복
    for _ in range(k):
        # 폭발
        grid, did_explode = explode_bombs(grid)
        
        # 이전 turn에서 폭발이 하나도 일어나지 않았으면 실행 중단
        if not did_explode:
            break
        
        grid = apply_gravity(grid)  # 중력 적용
        grid = rotate_90(grid)      # 회전
        grid = apply_gravity(grid)  # 회전 후 중력 적용
    
    # return : 남은 폭탄의 수
    for x in range(1, 101):
        for row in grid:
            left_bomb += row.count(x)
    return left_bomb
    
    # 이렇게도 작성이 되네요.... 신기해요
    # return sum(row.count(x) for x in range(1, 7) for row in grid)


# result    
result = solve_bomb_puzzle(grid, k)
print(result)

'''
python에서는 for문과 if문을 영문장처럼 한줄에..! 적을 수 있다는 걸 알게되었습니다..
그런데 어떤 방식이 바람직한지 모르겠네요
코드 가독성 측면에서 개인적으로는 for, if문을 풀어서 적는게 좋을 것 같은데,,,

---------------

아직 문제 다 해결하진 못했어요 .. 푸는중
잘못된 부분 고민중..
'''