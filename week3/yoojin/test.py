N = int(input())
num = []
result = []

for _ in range(N):
    line = input().split()
    command = line[0]

    if command == "push_back":
        num.append(int(line[1]))
    elif command == "pop_back":
        num.pop()
    elif command == "size":
        result.append(len(num))
    elif command == "get":
        result.append(int(num[int(line[1])-1]))

for item in result:
    print(item)