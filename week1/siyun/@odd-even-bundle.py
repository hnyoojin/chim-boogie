N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
i=0
even=0
odd=0
result=0
for i in range(N):
    if numbers[i]%2==0:
        even+=1
    else :
        odd+=1

while(True):
    if result%2==0:
        if even:
            even-=1
            result+=1
        elif odd>=2 :
            odd-=2
            result+=1
        else :
            if odd>0: 
                result-=1
            break
    else :
        if odd:
            odd-=1
            result+=1
        else : 
            break

print (result)
