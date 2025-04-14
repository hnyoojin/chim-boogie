n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

def pop():
    #터지기
    is_poped=False
    for x in range(n): #x축
        same_start=0
        same_count=1
        for y in range(1,n): #y축
            if numbers_2d[y][x]==numbers_2d[same_start][x] and numbers_2d[y][x] != 0:
                same_count+=1
                if y==n-1 and same_count>=m:
                    for i in range(same_count):
                        numbers_2d[same_start+i][x]=0
                        is_poped=True
            else: 
                if same_count>=m:
                     for i in range(same_count):
                        numbers_2d[same_start+i][x]=0
                        is_poped=True
                same_count=1
                same_start=y
    return is_poped

def fall():
    for x in range(n):
        #임시 배열
        tmp=[0]*n
        tmp_i=n-1

        #값이 있으면 임시배열 아래에서부터 넣기
        for y in range(n-1,-1,-1):
            if numbers_2d[y][x]>0:
                tmp[tmp_i]= numbers_2d[y][x]
                tmp_i-=1

        #임시 배열을 원래 배열로 복사
        for y in range(n):
            numbers_2d[y][x]=tmp[y]

# 터질 게 없을 때 까지 터트리기
def allpop():
    while pop():
        fall()

def boom(): 
    # m이 1이면 다 터지기 때문에 0
    if (m==1): return 0

    global numbers_2d
    for a in range(k):
        allpop()
            
        #회전
        numbers_2d=[list(row) for row in zip(*numbers_2d[::-1])]
        
        fall()
    allpop()
    

    return sum(1 for row in numbers_2d for x in row if x>0)

print(boom())
