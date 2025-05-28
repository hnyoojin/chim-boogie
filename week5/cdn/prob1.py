n = int(input())  # 선분 개수 입력받기
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())  # 각 선분의 양끝점 입력받기
    x1.append(a)
    x2.append(b)

lines = list(zip(x1, x2))  # 선분을 (시작점, 끝점) 튜플 리스트로 묶기

# 선분의 끝점을 기준으로 오름차순 정렬
# 끝점이 같으면 시작점 기준으로 오름차순 정렬
lines.sort(key=lambda x: (x[1], x[0]))

count = 0         # 선택한 선분의 개수
end = 0  # 이전에 선택한 선분의 끝점 (0으로 초기화)

for line_start, line_end in lines:
    # 이전 끝점보다 현재 선분 시작점이 커야 겹치지 않음
    if line_start > end:
        count += 1        # 선분 선택
        end = line_end     # 선택한 선분의 끝점 갱신

print(count)  # 겹치지 않게 고를 수 있는 최대 선분 수 출력
