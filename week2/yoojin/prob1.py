# 기울어진 직사각형
# apr 10 : 1h
# apr 11 : 3h+..

# input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# variant init
count_of_slanted_rect = 0
sum_of_current_rect = 0
max_sum_of_slanted_rect = 0
LD, RD, RU, LU = False, False, False, False

# def

# 다음 방향 탐색 함수
# start_i, j : 시작 지점의 좌표
def where_to_go(i, j, start_i, start_j):
    global LD, RD, RU, LU
    
    # 모든 방향으로 이동을 완료했고, 시작 지점으로 다시 돌아온 경우 
    # -> 결과 출력 함수 호출 -> 종료
    if LD and RD and RU and LU and i == start_i and j == start_j:
        print_result()
        return
        
    if not LD:
        left_down(i, j, start_i, start_j)
    elif LD and not RD:
        left_down(i, j, start_i, start_j)
        right_down(i, j, start_i, start_j)
    elif LD and RD and not RU:
        right_down(i, j, start_i, start_j)
        right_up(i, j, start_i, start_j)
    elif LD and RD and RU and not LU:
        right_up(i, j, start_i, start_j)
        left_up(i, j, start_i, start_j)
    """
        현재 문제 : LD True, RD False 인 경우에, 
        left_down이 성공한다면, 그 아래줄 코드인 right_down은 영원히 실행되지 않음

        시도할 방법 : DFS 구조를 도입해보는 것
    """


def print_result():
    global count_of_slanted_rect, max_sum_of_slanted_rect
    global current_route, LD, RD, RU, LU
    
    count_of_slanted_rect += 1
    del current_route[-1]
    sum_of_current_rect = sum(current_route)
    print(f"current route: {current_route}")
    print(f"sum of current rect = {sum_of_current_rect}")
    max_sum_of_slanted_rect = max(max_sum_of_slanted_rect, sum_of_current_rect)
    
    current_route = []
    LD, RD, RU, LU = False, False, False, False
    

def left_down(i, j, start_i, start_j):
    global LD, current_route
    
    ni, nj = i + 1, j - 1
    if ni >= n or nj < 0:
        return
    
    current_route.append(grid[ni][nj])
    LD = True
    where_to_go(ni, nj, start_i, start_j)

def right_down(i, j, start_i, start_j):
    global RD, current_route
    
    ni, nj = i + 1, j + 1
    if ni >= n or nj >= n:
        return
    
    current_route.append(grid[ni][nj])
    RD = True
    where_to_go(ni, nj, start_i, start_j)

def right_up(i, j, start_i, start_j):
    global RU, current_route
    
    ni, nj = i - 1, j + 1
    if ni < 0 or nj >= n:
        return
    
    current_route.append(grid[ni][nj])
    RU = True
    where_to_go(ni, nj, start_i, start_j)

def left_up(i, j, start_i, start_j):
    global LU, current_route
    
    ni, nj = i - 1, j - 1
    if ni < 0 or nj < 0:
        return
    
    current_route.append(grid[ni][nj])
    LU = True
    where_to_go(ni, nj, start_i, start_j)

for i in range(n):
    for j in range(n):
        current_route = [grid[i][j]]
        LD, RD, RU, LU = False, False, False, False
        where_to_go(i, j, i, j)

print(max_sum_of_slanted_rect)



'''
저는 시작지점을 00에서부터 n-1 n-1까지 순회시키면서,
각각 시작지점에 대해 LD -> RD -> RU -> LU 순서로 격자를 움직이도록 했습니다.

기울어진 사각형이라면 어느 방향으로, 어디서부터 순회하든 반드시 LD RD RU LU를 다 지나서 원점으로 돌아올거라 생각했음! (내가 맞음!)

그래서 일단 LD RD RU LU를 False로 주고, global 설정을 해서, 각각 LD RD RU LU 함수를 통과하면 True가 되도록 했음!

'''