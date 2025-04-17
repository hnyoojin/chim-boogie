'''
소요 시간 : 2h
'''

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

# 행렬 인덱스에 맞게 시작점 값 조정
r -= 1
c -= 1

# RU LU LD RD
dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]
lengths = [m1, m2, m3, m4]


path = []
x, y = r, c
for direction in range(4):
    for _ in range(lengths[direction]):
        x += dx[direction]
        y += dy[direction]
        if 0 <= x < n and 0 <= y < n:
            path.append((x, y))

# 값 회전시키기
values = [grid[x][y] for x, y in path]
if dir == 1:  # 시계
    values = values[1:] + [values[0]]
else:         # 반시계
    values = [values[-1]] + values[:-1]

# grid에 회전한 기울어진 직사각형의 값 적용
for i, (x, y) in enumerate(path):
    grid[x][y] = values[i]

# result print
for row in grid:
    print(*row)

'''
enumerate()라는 게 있더라고요!! 한번 사용해봤습니다
인덱스와 값을 동시에 순회할 수 있는 for문을 만들 수 있어요!

그리고 결과 출력 부분에서, * 는 리스트나 튜플같은 자료형의 요소를 하나하나 풀어주는 연산자입니당
'''