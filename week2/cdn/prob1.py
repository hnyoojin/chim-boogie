N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

# 아직 어떤 "기울어진 직사각형"도 검사하지 않았으니 max_sum을 0으로 설정
max_sum = 0

# 모든 가능한 시작점(v0)와 d1, d2 값 탐색
for i in range(N):
    for j in range(N):
        # d1, d2는 최소 1부터 시작
        for d1 in range(1, N):
            for d2 in range(1, N):
                # v0 : 시작점 (아래, 6시)
                v0 = (i, j)
                # v1 : 3시 방향
                v1 = (i - d2, j + d2)
                # v2 : 12시 방향
                v2 = (i - d2 - d1, j + d2 - d1)
                # v3 : 9시 방향
                v3 = (i - d1, j - d1)
                
                # 각 꼭짓점이 격자 내부에 있는지 확인
                # v0는 for문의 범위 내이므로 생략하고, v1, v2, v3만 체크
                # 만약 하나라도 격자를 벗어나면 continue로 다음 (d1, d2) 조합을 시도함 
                if v1[0] < 0 or v1[1] >= N:
                    continue
                if v2[0] < 0 or v2[1] >= N:
                    continue
                if v3[0] < 0 or v3[1] < 0:
                    continue

                # 경계선 좌표 채우기
                boundary = set()
                # (1) v0 -> v1: 이동 벡터 (-1, +1), d2번 이동 (0부터 d2까지 포함)
                for k in range(d2 + 1): # 변수 d2(N)까지 3시 방향으로 이동 
                    r, c = i - k, j + k
                    boundary.add((r, c))
                # (2) v1 -> v2: 이동 벡터 (-1, -1), d1번 이동
                for k in range(d1 + 1): # 변수 d1(N)까지 12시 방향으로 이동 
                    r, c = v1[0] - k, v1[1] - k
                    boundary.add((r, c))
                # (3) v2 -> v3: 이동 벡터 (+1, -1), d2번 이동
                for k in range(d2 + 1):  # 변수 d2(N)까지 9시 방향으로 이동 
                    r, c = v2[0] + k, v2[1] - k
                    boundary.add((r, c))
                # (4) v3 -> v0: 이동 벡터 (+1, +1), d1번 이동
                for k in range(d1 + 1):  # 변수 d1(N)까지 6시 방향으로 이동 (제자리)
                    r, c = v3[0] + k, v3[1] + k
                    boundary.add((r, c))
                
                # (디버깅) 현재 후보 경계 출력
                # print("v0", v0, "v1", v1, "v2", v2, "v3", v3)
                # print("Boundary:", boundary)

                # 결과
                # v0 (3, 2) v1 (2, 3) v2 (0, 1) v3 (1, 0)
                # Boundary: {(3, 2), (2, 3), (1, 2), (0, 1), (1, 0), (2, 1)}

                # 경계에 포함된 격자 셀들의 합 계산
                current_sum = 0
                valid = True
                for r, c in boundary:
                    # 혹시라도 경계를 벗어난 좌표가 들어갔다면 스킵
                    if r < 0 or r >= N or c < 0 or c >= N:
                        valid = False
                        break
                    current_sum += grid[r][c]
                if not valid:
                    continue
                
                # 최댓값 갱신
                max_sum = max(max_sum, current_sum)

# 결과 출력
print(max_sum)

