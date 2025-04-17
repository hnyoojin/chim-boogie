n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


'''
제일 위의 꼭지점(dot)이 이동함.

     * (dot)
  one four
 *       *
  two three
     *

이 순서로 순회하며 숫자를 합해서 최대값을 구함
three는 one이 이동한 거리만큼 이동. (갈 수 없는 경우 three,two 취소하고 one으로 돌아감)
four는 two가 이동한 거리만큼 이동. dot에 도착하면 dot값은 두 번 더했으니 한번 빼줌
'''

max_result=0


# 꼭지점 y축 이동
for y in range(n-2):
    # 꼭지점 x축 이동
    for x in range(1,n-1):
        dot = grid[y][x]
        
        # y축 아래로 직사각형을 그릴 수 있다면
        if y<n-2:

            # one 
            oneY, oneX = y+1 , x-1
            one = dot
            one_count = 0 # one이 이동한 횟수
            while oneY < n-1 and oneX >= 0 :
                one += grid[oneY][oneX]
                one_count += 1
                #print("one이동",grid[oneY][oneX])

                # two
                twoY, twoX = oneY+1, oneX+1
                two = one
                two_count = 0 # two가 이동한 횟수
                while twoY < n and twoX < n-1:
                    two += grid[twoY][twoX]
                    two_count +=1
                    #print("two이동", grid[twoY][twoX])

                    # three
                    threeY, threeX = twoY-1, twoX+1
                    three = two
                    three_count = 0
                    isbreak = False
                    # one이 간 거리까지 이동
                    while three_count < one_count:
                        three += grid[threeY][threeX]
                        three_count+=1
                        if three_count != one_count:
                            threeY -= 1
                            threeX += 1
                        # 갈 수 없으면 다시 one으로 회귀
                        if  threeX > n-1:
                            isbreak = True
                            break
                    if isbreak :
                        break

                    # four
                    fourY, fourX = threeY-1, threeX-1
                    four = three
                    four_count = 0
                    # two가 간 거리까지 이동
                    while four_count < two_count:
                        four += grid[fourY][fourX]
                        four_count+=1
                        if four_count != two_count:
                            fourY -= 1
                            fourX -= 1
                    
                    # dot에 한번 더 갔으니 빼주기
                    four-=dot

                    if four > max_result:
                        max_result = four

                    twoX+=1
                    twoY+=1

                oneY+=1
                oneX-=1

print(max_result)


            
