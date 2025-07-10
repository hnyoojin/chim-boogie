# N : 보석 개수
# M : 배낭 수용 한계
# w : 보석의 정보 - 무게
# v : 보석의 정보 - 가치

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

max_value = [0] * (M+1)

for i in range(N):
    # 앞에서부터 보석 살펴보기
    weight = w[i]
    value = v[i]

    # for 문을 거꾸로 돌려서 중복 제거
    for j in range(M, weight-1, -1):
        # 최대 가치 비교 (보석 포함 시켰을 때 vs 보석 포함 안 시켰을 때)
        max_value[j] = max(max_value[j], max_value[j-weight]+value)

print(max_value[M])