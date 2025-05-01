n = int(input())

def is_valid(sequence):
    length = len(sequence)
    
    for i in range(1, length // 2 + 1):
        if sequence[length - i:] == sequence[length - 2*i:length - i]:
            return False
    
    return True

def find_min_sequence(n):
    sequence = []
    
    def backtrack():
        if len(sequence) == n:
            return True
        
        for num in [4, 5, 6]:
            sequence.append(num)
            
            if is_valid(sequence):
                if backtrack():
                    return True
            
            sequence.pop()
        
        return False
    
    backtrack()
    return sequence

result = find_min_sequence(n)
print(''.join(map(str, result)))
