'''
최고의 33위치

N X N 크기의 격자 위에서, 3 X 3 크기의 격자 안에 들어가는 수의 합이 최대가 될 때의 값을 출력
'''

# input
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# variant init
max_3x3 = 0

# def
def get_3x3_sum(i, j):
    return grid[i][j] + grid[i][j+1] + grid[i][j+2] \
        + grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] \
        + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]

# code
for j in range(n-2):
    for i in range(n-2):
        max_3x3 = max(max_3x3, get_3x3_sum(i,j))

# print result
print(max_3x3)


'''
3 x 3 격자 합을 구할때, 저렇게 9개를 하나하나 더하는 것 말고 더 간결하고 명확한 코드를 짤 수 있으면 좋을 것 같은데,,
아직 제 실력이 거기까지 미
'''