import sys

# 입력 및 초기 설정
n = int(input().strip())     # 수열의 길이
numbers = [4, 5, 6]          # 사용 가능한 숫자
series = []                  # 현재까지 만든 수열

def is_possible_series():
    """
    series의 꼬리 부분을 검사하여,
    인접한 두 개의 연속 부분 수열이 같은 경우가 없는지 확인합니다.
    """
    length = 1
    while True:
        # 뒤에서부터 길이 length인 두 구간의 시작/끝 인덱스 계산
        start1, end1 = len(series) - length, len(series) - 1
        start2, end2 = start1 - length, start1 - 1

        # 비교할 두 번째 구간이 수열 밖으로 나가면 중단
        if start2 < 0:
            break

        # 두 구간이 같으면 불가능한 수열
        if series[start1:end1 + 1] == series[start2:end2 + 1]:
            return False

        length += 1

    return True

def find_min_series(cnt):
    """
    깊이 우선 탐색으로 길이 n짜리 수열을 만들면서
    조건을 만족하면 즉시 출력하고 종료합니다.
    """
    # 기저 조건: 길이가 n이 되면 결과 출력 후 종료
    if cnt == n:
        print(''.join(map(str, series)))
        sys.exit(0)

    # 4, 5, 6을 순서대로 시도 (사전순 보장)
    for number in numbers:
        series.append(number)
        # 지금까지 만든 수열이 조건을 만족하면 재귀 계속
        if is_possible_series():
            find_min_series(cnt + 1)
        # 백트래킹: 마지막에 추가한 숫자 되돌리기
        series.pop()

# 탐색 시작
find_min_series(0)
