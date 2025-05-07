n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

ans=0
# Please write your code here.

# 물건들 합이 c를 넘을 때 물건 고르기
def choice(items, i, max_sum, choice_items):
    if i >= len(items): 
        return max_sum  #더 이상 탐색할 물건이 없다면 현재까지의 max_sum을 반환

    #1. 합이 c 이하인지
    if sum(choice_items) + items[i] <= c: 
        #2. 가치 최대값인지
        choice_items.append(items[i])

        value_sum = sum(x ** 2 for x in choice_items)  
        if value_sum > max_sum:
            max_sum=value_sum

        max_sum=choice(items, i+1, max_sum, choice_items) 

        choice_items.pop()

    max_sum = choice(items, i+1, max_sum, choice_items) 

    return max_sum

# 물건 가치 반환 
def get_value(items):
    if sum(items)>c:
        return choice(items,0,0,[])
    return sum(x**2 for x in items)


# 최대가치 갱신하기
def update_max(a,b):
    global ans
    value_sum=0
    a_items=weight[a[0]][a[1]:a[1]+m]
    b_items=weight[b[0]][b[1]:b[1]+m]
    a_items.sort(reverse=True)
    b_items.sort(reverse=True)
    value_sum+=get_value(a_items)
    value_sum+=get_value(b_items)
    ans=max(value_sum,ans)
    return 

#자리 옆으로 한칸씩 옮기기
def move(loc):
    new_loc = list(loc)
    if new_loc[1] >= n - m:
        new_loc[0] += 1
        new_loc[1] = 0
    else:
        new_loc[1] += 1
    if new_loc[0] >= n or new_loc[1]>n-m: return None
    return tuple(new_loc)

finish=False
def go (a,b):
    global finish
    #B가 끝에 왔으면 return
    if b is None or a is None or finish:
        return
    update_max(a,b)

    #A는 두고 B만 움직임
    b=move(b)
    go(a,b)

    if not finish:
        #A전진 B는 A다음 위치에
        a=move(a)
        if a is not None:
            b = move((a[0], a[1] + m - 1))
            if b is not None:
                go(a, b)
            #A 다음 B가 끝에 도달하면 종료
            else: finish=True

#A와 B의 초기 위치를 전달
go((0,0),move((0,0+m-1)))
print(ans)
