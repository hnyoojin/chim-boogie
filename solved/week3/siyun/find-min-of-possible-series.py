n = int(input())

# Please write your code here.
arr=[]
is_find=False

def possible_print(cnt):
    global ans, is_find
    #길이 다 채우면 찾은거니 종료
    if cnt ==n: 
        is_find =True
        return
    else:
        for i in range (4,7):
            # if is_find==True: return
            is_possible=True
            # 불가능 수열 걸러내기
            arr.append(i)
            #
            if cnt>=1 and arr[cnt-1]==arr[cnt]:
                arr.pop()
                is_possible=False
            else :
                for j in range(1,(cnt+1)//2):
                #비교 대상의 개수가 충분할 때
                    if (cnt+1)//2>j:
                        if arr[cnt-(j*2)-1:cnt-j]==arr[cnt-j:cnt+1]:
                            arr.pop()
                            is_possible=False
                            break

            if is_possible is False: continue
            possible_print(cnt+1)
            if is_find is True: return
            arr.pop()

possible_print(0)
print(*arr, sep='')
