import sys
# 매우 큰 숫자 입력 처리 시 문자열 길이 제한 해제 (기본 제한이 있어서 큰 수 입력 시 오류 방지)
sys.set_int_max_str_digits(10**7)

n = input().strip()  # 문자열로 입력받은 숫자
length = len(n)      # 숫자의 자릿수

MOD = 10**9 + 7      # 결과값 나머지 연산에 사용할 큰 소수

# dp 배열 선언
# dp[pos][is_less][has_clap][digit_sum_mod3]
# pos: 현재 자리 위치 (0부터 length까지)
# is_less: 지금까지 만든 숫자가 입력 숫자 n보다 작으면 1, 아니면 0 (bool)
# has_clap: 지금까지 숫자에 3,6,9가 포함되어 있으면 1, 아니면 0 (bool)
# digit_sum_mod3: 지금까지 자리 숫자들의 합을 3으로 나눈 나머지 (0,1,2)
# 저장 값: 해당 상태까지 만들어진 숫자의 개수 (경우의 수)
dp = [[[[0]*3 for _ in range(2)] for _ in range(2)] for _ in range(length+1)]

# 초기 상태: 아직 아무 숫자도 고르지 않은 상태
# pos=0, is_less=0 (아직 n과 같음), has_clap=0 (아직 3,6,9 없음), digit_sum_mod3=0 (합 0)
dp[0][0][0][0] = 1

for pos in range(length):           # 각 자리수 위치에 대해 반복
    limit = int(n[pos])             # 해당 자리의 최대 숫자 (입력 숫자의 자리 숫자)
    for is_less in range(2):        # 이전까지 숫자가 n보다 작았는지 여부
        for has_clap in range(2):  # 3,6,9 포함 여부
            for digit_sum_mod3 in range(3):  # 지금까지 숫자 합의 mod 3 상태
                current_count = dp[pos][is_less][has_clap][digit_sum_mod3]
                if current_count == 0:
                    continue          # 현재 상태에 도달한 경우가 없으면 건너뜀

                # 다음 자리에 올 수 있는 숫자 범위 설정
                # 만약 이전 숫자가 n보다 작아졌다면 제한 없이 0~9 모두 가능
                # 아니라면 현재 자리 숫자 최대값으로 제한
                max_digit = 9 if is_less else limit

                for d in range(max_digit+1):  # 다음 자리 숫자 d 선택
                    # 새로운 상태 계산
                    # new_is_less: 이미 작았거나, 이번 자리 숫자가 제한 숫자보다 작으면 True
                    new_is_less = is_less or (d < max_digit if not is_less else False)
                    # new_has_clap: 기존에 3,6,9 포함했거나 이번 자리 숫자가 3,6,9인지 여부
                    new_has_clap = has_clap or (d in [3,6,9])
                    # new_digit_sum_mod3: 기존 합에 이번 숫자 더한 후 3으로 나눈 나머지
                    new_digit_sum_mod3 = (digit_sum_mod3 + d) % 3

                    # 해당 상태의 경우의 수 누적 (mod 연산)
                    dp[pos+1][new_is_less][new_has_clap][new_digit_sum_mod3] = \
                        (dp[pos+1][new_is_less][new_has_clap][new_digit_sum_mod3] + current_count) % MOD

# 모든 자릿수 선택 후 (pos=length) 가능한 숫자 중
# 박수 조건 (3,6,9 포함 OR 숫자 합이 3의 배수) 인 경우의 수 합산
result = 0
for is_less in range(2):
    for has_clap in range(2):
        for digit_sum_mod3 in range(3):
            # 박수 조건에 부합하는 경우만 합산
            if has_clap or digit_sum_mod3 == 0:
                result = (result + dp[length][is_less][has_clap][digit_sum_mod3]) % MOD

# 0은 포함 안 하므로 결과에서 1 빼기 (0은 3,6,9 없고 3의 배수도 아님)
result -= 1
if result < 0:
    result += MOD

print(result)
