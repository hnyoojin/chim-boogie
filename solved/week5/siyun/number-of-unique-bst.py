n = int(input())

dp=[1]*(n+1)
# Please write your code here.

#즉, 루트를 k로 고정하면,
#왼쪽 서브트리로 만들 수 있는 BST의 개수 × 오른쪽 서브트리로 만들 수 있는 BST의 개수가
#루트를 k로 할 때 만들 수 있는 BST 개수가 되는 것
# dp[0] = 1 (노드가 없을 때도 하나의 BST로 본다)
# dp[1] = 1
# dp[2]=dp[1]*2
# dp[3]=dp[2]*2+dp[1]
# dp[4]=dp[3]*2+(dp[1]*dp[2])*2
# dp[5]=dp[4]*2+(dp[1]*dp[3])*2+(dp[1]*dp[2])*2
# dp[6]=dp[5]*2+(dp[1]*dp[4])*2+(dp[2]*dp[3])*2

# 점화식
# dp[i]=(dp[0]*dp[i-1])*2+(dp[1]*dp[i-2])*2+(dp[2]*dp[i-3])*2+...
# 만약 i가 홀수면 dp[j]와 dp[i-(j+1)]이 같아질때 + dp[j]*dp[j]해줌

for i in range (1, n+1):
    sum=0
    for j in range(0,(i//2)+(i%2)):
        if j==i-(j+1) : sum+=(dp[j]*dp[j])
        else : sum+=(dp[j]*dp[i-(j+1)])*2
    dp[i]=sum

print (dp[n])


#카탈린 수 점화식은 이건데 대칭되는 부분 중복계산이 들어가게 됨
#dp[0]=1
#dp[1]=dp[0]*dp[0]
#dp[2]=dp[0]*dp[1]+dp[1]*dp[0]

# for i in range(1,n+1):
#     sum=0
#     for j in range (i):
#         sum+=dp[j]*dp[(i-1)-j]
#     dp[i]=sum
