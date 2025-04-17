n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())


# Please write your code here.

#헐
r-=1
c-=1

# 시계방향
if dir==1:
    #dot
    tmp = grid[r][c]
    #one 반대방향
    one_count=0
    for i in range(m1):
        grid[r][c] = grid[r-1][c+1]
        r-=1 
        c+=1
    #two 반대방향
    for i in range(m2):
        grid[r][c] = grid[r-1][c-1]
        r-=1 
        c-=1
    #three 반대방향
    for i in range(m3):
        grid[r][c] = grid[r+1][c-1]
        r+=1 
        c-=1
     #four 반대방향
    for i in range(m4-1):
        grid[r][c] = grid[r+1][c+1]
        r+=1 
        c+=1
    grid[r][c] = tmp
else :
    tmp = grid[r][c]
    #four
    for i in range(m4):
        grid[r][c] = grid[r-1][c-1]
        r-=1 
        c-=1
    #three
    for i in range(m3):
        grid[r][c] = grid[r-1][c+1]
        r-=1 
        c+=1
    #two
    for i in range(m2):
        grid[r][c] = grid[r+1][c+1]
        r+=1 
        c+=1
    #one
    for i in range(m1-1):
        grid[r][c] = grid[r+1][c-1]
        r+=1 
        c-=1
    grid[r][c] = tmp



for a in grid :
    print (*a)
