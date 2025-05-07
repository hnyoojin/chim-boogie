n, m = map(int, input().split())
lines=list()
selected_lines = list()

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))
lines.sort()

#처음 상황과, 선택한 가로줄만 사용했을 때의 상황을 시뮬레이션 후 비교
def possible():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]

    for _,idx in lines:
        num1[idx], num1[idx+1]=num1[idx+1],num1[idx]
    for _,idx in selected_lines:
        num2[idx], num2[idx+1]=num2[idx+1],num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return False
    return True

min_line=m
#사다리 한줄씩 그리기
def draw_min_line(line_count):
    global min_line

    if line_count==m:
        if possible():
            min_line=min(min_line,len(selected_lines))
        return 
    # 라인 그리기
    selected_lines.append(lines[line_count])
    draw_min_line(line_count+1)
    selected_lines.pop()
    draw_min_line(line_count+1)




draw_min_line(0)
print(min_line)
