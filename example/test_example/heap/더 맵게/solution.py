def solution(scoville, K):
    answer = 0
    iter_ = 0

    while scoville[0] < k:
        if len(scoville) >= 2:
            scoville.sort()
            first_min = scoville[0]
            second_min = scoville[1]
            mix_ = first_min + (second_min*2)
            scoville.append(mix_)

            iter_ += 1
        else:
            answer = -1
            return answer

    answer = iter_
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

answer = solution(scoville, K)
print(answer)
