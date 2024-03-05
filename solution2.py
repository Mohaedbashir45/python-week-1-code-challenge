def digit_sum(number):
    # calculate the sum of digits of a number
    return sum(int(digit) for digit in str(number))

def solution(A):
    # Create a dictionary to store numbers 
    digit_sums = {}
    
    for number in A:
        # Calculate the sum of digits of the current number
        sum_of_digits = digit_sum(number)
        
        if sum_of_digits in digit_sums:
            digit_sums[sum_of_digits] = max(digit_sums[sum_of_digits], number)
        else:
            digit_sums[sum_of_digits] = number
    
    max_sum = -1
    
    for key, value in digit_sums.items():
        if key * 2 > max_sum and key in digit_sums and key != 0:
            max_sum = max(max_sum, value + digit_sums[key])
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42])) # Output: 93
print(solution([42, 33, 60])) # Output: 102
print(solution([51, 32, 43])) # Output: -1
