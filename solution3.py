def solution(N):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    i = 0
    while len(result) < N:
        result += alphabet[i] * (N // 26 + (i < N % 26))
        i += 1
    return result[:N]

# Test cases
print(solution(3))  # Output can be "abc", "def", etc.
print(solution(5))  # Output can be "abcde", "fghij", etc.
print(solution(30)) # Output can be "aabbccddeeffgghhiijjkkllmmnnoo"

