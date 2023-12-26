# solution 1
def solution1(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution1(numbers[1:], target-numbers[0]) + solution1(numbers[1:], target+numbers[0])
    
# solution 2
from itertools import product
def solution2(numbers, target):
    l = [(x,-x)for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# solution 3
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx == N and target == value):
        answer += 1
        return
    if(idx == N):
        return
    
    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])

def solution(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer