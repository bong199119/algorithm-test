def solution(array, commands):
    answer = []

    for command in commands:
        idx_start = command[0]-1
        idx_end = command[1]
        idx_target = command[2]

        array_target = array[idx_start:idx_end]
        array_target.sort()
        number_target = array_target[idx_target-1]
        answer.append(number_target)

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(array, commands)
print(answer)
