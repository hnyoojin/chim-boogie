def simulate_ladder(N, lines):
    """
    사다리 정보를 이용해 1~N이 아래로 내려갔을 때
    최종 위치를 계산해 반환하는 함수입니다.
    - N: 세로줄 개수
    - lines: [(a, b), ...] 형태의 리스트
        * b 높이에서 a번과 a+1번 세로줄이 연결됨을 의미
    """
    # ➊ 사다리를 위에서부터(높이 b가 작은 순) 처리하도록 정렬
    '''
    여기서 key= 란?
    sort() 메서드는 기본적으로 리스트의 원소를 그 자체로 비교해서 정렬함
    튜플 (a,b)가 들어있는 경우 첫번째 요소인 a로만 비교하면 b 순서대로 정렬되지 않음
    그래서 key=lambda x: x[1] 은 x 가 (a,b) 일 때, 돌려주는 값이 x[1], 즉 b가 되도록 함
    '''
    
    lines.sort(key=lambda x: x[1])
    
    # ➋ p[i] = i+1 로 초기화 → 사람 번호 1,2,…,N
    p = list(range(1, N + 1))
    
    # ➌ 정렬된 가로줄 정보를 차례대로 읽어 스왑 처리
    for a, _ in lines:
        # a번 세로줄 위치의 사람과 a+1번 위치의 사람을 맞바꿈
        # 리스트 인덱스는 0부터 시작하므로 a-1과 a를 사용
        p[a - 1], p[a] = p[a], p[a - 1]
    
    # ➍ 최종 배열 반환
    return p

def count_inversions(arr):
    """
    배열 arr에 대해 inversion(뒤집힌 쌍) 개수를 세어 반환합니다.
    inversion 수 = 정렬(오름차순)으로 되돌리기 위한
    최소 adjacent swap(인접 교환) 횟수와 동일합니다.
    """
    inv = 0
    n = len(arr)
    # ⓵ 모든 i < j 쌍을 검사
    for i in range(n):
        for j in range(i + 1, n):
            # ⓶ 앞의 값이 뒤의 값보다 크면 뒤집힌 쌍
            if arr[i] > arr[j]:
                inv += 1
    return inv

# ─────────────────────────────────────────────
# 입력 처리
# ─────────────────────────────────────────────
# 한 줄에 n, m이 주어지고
n, m = map(int, input().split())
# 다음 m줄에는 a, b 형태로 가로줄 정보가 주어집니다.
lines = [tuple(map(int, input().split())) for _ in range(m)]

# ─────────────────────────────────────────────
# 사다리 시뮬레이션 & inversion 계산
# ─────────────────────────────────────────────
final_pos = simulate_ladder(n, lines)
# simulate_ladder: 1~n이 사다리 내려간 뒤 최종 위치 리스트

answer = count_inversions(final_pos)
# count_inversions: 최종 위치를 [1,2,…,n]으로 정렬하는 데 필요한 스왑 횟수

# ─────────────────────────────────────────────
# 결과 출력
# ─────────────────────────────────────────────
print(answer)
