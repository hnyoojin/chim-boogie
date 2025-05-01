n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]


# 메인 함수
def solution(n, m, edges):
    # 사다리 최대 높이
    max_height = max(b for a, b in edges) if edges else 0
    
    # 사다리 행렬 만들기
    ladder = [[0] * n for _ in range(max_height + 1)]
    for a, b in edges:
        ladder[b][a-1] = 1
    
    # 가로줄 M개 결과
    origin_result = []
    for start in range(n):
        end = ladder_game(ladder, start)
        origin_result.append(end)
    
    # 최소 가로줄 개수 찾기
    min_count = find_min_edges(n, edges, origin_result, max_height)
    
    return min_count

# 사다리 시뮬레이션 돌려보는 함수
def ladder_game(board, start):
    current = start
    
    for row in range(1, len(board)):
        # 현재 위치에 가로줄이 있으면 오른쪽으로 이동
        if current < len(board[0])-1 and board[row][current] == 1:
            current += 1
        # 왼쪽에 가로줄이 있으면 왼쪽으로 이동
        elif current > 0 and board[row][current-1] == 1:
            current -= 1
    
    return current

# 가로줄 최소 개수 찾기 함수
def find_min_edges(n, edges, target_results, max_height):
    min_count = float('inf')
    
    def check_subset(index, current_edges):
        nonlocal min_count
        
        if len(current_edges) >= min_count:
            return
        
        if index == len(edges):
            board = [[0] * n for _ in range(max_height + 1)]
            for i in current_edges:
                a, b = edges[i]
                board[b][a-1] = 1
            
            current_results = []
            for start in range(n):
                end = ladder_game(board, start)
                current_results.append(end)
            
            if current_results == target_results:
                min_count = min(min_count, len(current_edges))
            
            return
        
        check_subset(index + 1, current_edges)
        check_subset(index + 1, current_edges + [index])
    
    check_subset(0, [])
    
    return min_count if min_count != float('inf') else -1



print(solution(n, m, edges))
