# 기울어진 직사각형
# apr 10 : 1h
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

count_of_slanted_rect = 0
sum_of_current_rect = 0
max_sum_of_slanted_rect = 0
current_route = []
LD, RD, RU, LU = False, False, False, False


def where_to_go(i, j):
    global LD, RD, RU, LU
    global count_of_slanted_rect
    global current_route
    global max_sum_of_slanted_rect

    if LD == False:
        left_down(i, j)
    if LD == True:
        left_down(i, j)
        right_down(i, j)
    elif RD == True:
        right_down(i, j)
        left_up(i, j)
    elif RU == True:
        right_up(i, j)
        left_up(i, j)
    elif LU == True:
        left_up(i, j)
    else:
        print_result()

def print_result():
    global count_of_slanted_rect
    global current_route
    global max_sum_of_slanted_rect

    count_of_slanted_rect += 1
    sum_of_current_rect = sum(current_route)
    
    current_route = []
    max_sum_of_slanted_rect = max(max_sum_of_slanted_rect, sum_of_current_rect)

def left_down(i, j):
    global LD
    global current_route
    i += 1
    j -= 1
    
    if i > n-1 or j < 0:
        if LD == True:
            where_to_go(i-1, j+1)
        else:
            current_route = []
            return
    else:
        current_route.append(grid[i][j])
        LD = True
        where_to_go(i, j)

def right_down(i, j):
    global RD
    global current_route
    i += 1
    j += 1
    
    if i > n-1 or j > n-1:
        if RD == True:
            current_route = []
            where_to_go(i-1, j-1)
        else:
            return
    else:
        current_route.append(grid[i][j])
        RD = True
        where_to_go(i, j)


def right_up(i, j):
    global RU
    global current_route
    i -= 1
    j += 1
    
    if i < 0 or j > n-1:
        if RU == True:
            current_route = []
            where_to_go(i+1, j-1)
        else:
            return
    else:
        current_route.append(grid[i][j])
        RU = True
        where_to_go(i, j)


def left_up(i, j):
    global LU
    global current_route
    i -= 1
    j -= 1
    
    if i < 0 or j < 0:
        if LU == True:
            current_route = []
            where_to_go(i+1, j+1)
        else:
            return
    else:
        current_route.append(grid[i][j])
        LU = True
        where_to_go(i, j)


for i in range(n):
    for j in range(n):
        current_route.append(grid[i][j])
        LD, RD, RU, LU = False, False, False, False
        where_to_go(i, j)

print(max_sum_of_slanted_rect)