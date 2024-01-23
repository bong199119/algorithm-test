def solution(participant, completion):
    answer = ''
    # completion_copy = completion[:]
    for part in completion:
        participant.remove(part)

    answer = participant[0]
    return answer

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append('none')

    for idx, part in enumerate(participant):
        if part != completion[idx]:
            answer = part
            break

    return answer


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = solution(participant, completion)
print(answer)

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

answer = solution(participant, completion)
print(answer)

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = solution(participant, completion)
print(answer)