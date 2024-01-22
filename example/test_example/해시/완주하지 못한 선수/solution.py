def solution(participant, completion):
    answer = ''
    participant_copy = participant[:]
    for part in participant:
        if part in completion:
            participant_copy.remove(part)

    answer = participant_copy[0]
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