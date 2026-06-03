def solution(A, B):
    stack = []    # peces → esperando rivales
    survivors = 0 # peces ← que sobrevivieron

    for size, direction in zip(A, B):
        if direction == 1:        # va →, al stack
            stack.append(size)
        else:                     # va ←, pelea
            while stack:
                if stack[-1] > size:  # pierde
                    break
                else:                 # gana, siguiente rival
                    stack.pop()
            else:                     # while terminó sin break → stack vacío
                survivors += 1

    return len(stack) + survivors


# Tests
print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))  # 2
print(solution([1, 2, 3, 4],    [1, 1, 1, 1]))      # 4
print(solution([4, 3, 2, 1],    [0, 0, 0, 0]))      # 4
print(solution([5, 4, 3, 2, 1], [1, 1, 0, 0, 0]))   # 2