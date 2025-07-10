def is_vps(s):
    count = 0
    for char in s:
        if char == '(': 
            count += 1
        elif char == ')': 
            count -= 1
            if count < 0: return 'NO'
    
    return 'YES' if count == 0 else 'NO'

n = int(input())
result = []

for _ in range(n):
    user_input = input().strip()
    result.append(is_vps(user_input))

for res in result:
    print(res)