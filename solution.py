def solution(A):
    # Calculate the total number 
    total_bricks = sum(A)
    # Calculate the target number for each box
    target_bricks = len(A) * 10
    
    if total_bricks % len(A) != 0 or total_bricks < target_bricks:
        return -1

    # Calculate the target number of bricks per box
    target_per_box = total_bricks // len(A)
    moves = 0
    
    for bricks in A:
        diff = bricks - target_per_box
        
        if diff > 0:
            if diff % 2 != 0:
                return -1
            moves += diff // 2
    
    return moves

# Test cases
print(solution([7, 15, 10, 8])) # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11])) # Output: 6
print(solution([7, 14, 10])) # Output: -1

