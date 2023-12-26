def solution(answers):
    no_math = [[]]*3
    no_math[0] = [1,2,3,4,5] * -(-len(answers) // 5)
    no_math[1] = [2,1,2,3,2,4,2,5] * -(-len(answers) // 8)
    no_math[2] = [3,3,1,1,2,2,4,4,5,5] * -(-len(answers) // 10)
    correct = [0]*3

    print(no_math)

    for i in range(len(answers)):
        for j in range(3):
            if no_math[j][i] == answers[i]:
                correct[j] += 1
    M = max(correct)

    return [x+1 for x in range(len(correct)) if correct[x] == M]


answers = [1,2,3,4,1,3,3,3,3,2,3,4]

print(solution(answers))