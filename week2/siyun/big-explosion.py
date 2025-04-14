n, m, r, c = map(int, input().split())

# Please write your code here.
dir=[(-1,0),(0, 1), (1,0),(0,-1)]
grid = [[0 for _ in range (n)] for _ in range(n)]
grid[r-1][c-1]=1


# 놓여져 있는 전체 폭탄 위치 리스트
boom_list=[]
boom_list.append((r-1,c-1))


def lets_boom ():
    for time in range (1,m+1):
        # 새로운 초가 시작할 시점의 폭탄 개수로 새로운 폭탄을 추가함
        boom_count=len(boom_list)
        for i in range (boom_count):
            # 4방향으로 폭탄 추가
            for d in dir:
                dy=boom_list[i][0]+d[0]*(2**(time-1))
                dx=boom_list[i][1]+d[1]*(2**(time-1))
                # 폭탄을 추가할 수 있으면 추가
                if dy>=0 and dy <n and dx>=0 and dx<n and grid[dy][dx]==0:
                    grid[dy][dx]=1
                    boom_list.append((dy,dx))

                    

                    

lets_boom()
print(len(boom_list))


            
            
