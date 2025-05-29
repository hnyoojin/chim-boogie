n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a,b))

# Please write your code here.
dp=[1]*n
#dp[i] = i번째 선분을 골랐을 때 지금까지 최대로 선택한 선분 갯수
#정렬 필요함

lines.sort(key =lambda x:x[1])

for i in range(n):
    for j in range(i):
        if lines[j][1]<lines[i][0]:
          #i와 겹치지 않는 j가 여러 개일 수 있고, 그 중 가장 큰 dp[j]를 기반으로 갱신
            dp[i]=max(dp[i],dp[j]+1)           


print(max(dp))
