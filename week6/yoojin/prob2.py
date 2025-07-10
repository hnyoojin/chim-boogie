# ....... test case 보니까 DP 쓰는 거 말곤 방법이 없는 것 같은데 도저히 DP 를 어떻게 써야할지 모르겠어요
# 일단 이렇게 하면 int로 형변화 되는 작은 입력까지는 처리 가능한데,,, 이건 쉬운데,,,

# n : 목표 숫자
# result : n 까지의 "짝" 회수

n = input()
result = 0

for i in range(1, int(n)+1):
    nums = [int(num) for num in str(i)]
    sum_of_num = 0
    
    j = len(nums)-1
    while j >= 0:
        sum_of_num += nums[j]
        if nums[j] == 3 or nums[j] == 6 or nums[j] == 9:
            result += 1
            break
        j -= 1

    else:
        if sum_of_num%3 == 0:
            result += 1

print(result % 1000000007)