# 기울어진 직사각형
# apr 10 : 1h
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

LD, RD, RU, LU = False, False, False, False
current_route = []
routes_of_slanted_rect = []
sum_of_slanted_rect = []
max_sum_of_slanted_rect = 0
count_of_slanted_rect = 0

def where_to_go():
    if LD == False:
        left_down()
    elif RD == False:
        right_down()
    elif RU == False:
        right_up()
    elif LU == False:
        left_up()
    else:
        print_result()

def print_result():
    print(max(sum_of_slanted_rect))

def left_down(i, j):
    i += 1
    j -= 1
    if i>n-1 or j<0: # can't go L/D
        if LD==True:
            right_down(i-1, j+1)
        else: 
            return
    else:
        current_route.append(grid[i][j])
        LD = True
        left_down()
        right_down()


def right_down(i, j):
    i += 1
    j -= 1
    RD = True
    where_to_go()

def right_up(i, j):
    i += 1
    j += 1
    RU = True
    where_to_go()

def left_up(i, j):
    i -= 1
    j += 1
    LU = True
    where_to_go()


# code
for i range(n):
    for j range(n):
        current_route.append(grid[i][j])
        where_to_go()

if LD and RD and RU and LU == True:
    max_sum_of_slanted_rect = max(max_sum_of_slanted_rect, sum_of_slanted_rect)
    LD, RD, RU, LU = False, False, False, False
    