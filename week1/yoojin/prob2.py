'''
N x N의 격자에서, 같은 숫자가 연속 M개 이상 나오는 경우의 수
를 행복한 수열이라고 한답니다
행복한 수열의 수 구하기..~
'''

# input
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grid_T = list(zip(*grid))

# variant init
count_of_happy_list = 0

# def
def find_happy_list(target, i):
    # 결과값 전역변수로 설정
    global count_of_happy_list
    
    j = 1
    count = 1
    
    while j < n:
        if target[i][j] != target[i][j-1]:
            count = 1
        else:
            count += 1
        j += 1

        if count == m:
            count_of_happy_list += 1
            break

# code
if m == 1:
    count_of_happy_list = n * 2
elif m > n:
    count_of_happy_list = 0
else:
    for i in range(n):
        find_happy_list(grid, i)
        find_happy_list(grid_T, i)

# print result
print(count_of_happy_list)