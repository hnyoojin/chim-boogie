# 입력 처리
n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# 선분 정보 line에 저장
line = list(zip(x1, x2))

# 선분 
line.sort(key=lambda x: x[1])

# 그리디 선택
count = 0
end = -1

for start, finish in line:
    if start > end:
        count += 1
        end = finish

print(count)
