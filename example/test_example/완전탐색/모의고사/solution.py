def solution(answers):
    answer = []
    
    ans_1_pattern = [1,2,3,4,5]
    ans_2_pattern = [2,1,2,3,2,4,2,5]
    ans_3_pattern = [3,3,1,1,2,2,4,4,5,5]
    
    ans_1 = (ans_1_pattern*((len(answers)//len(ans_1_pattern))+1))[:len(answers)]
    ans_2 = (ans_2_pattern*((len(answers)//len(ans_2_pattern))+1))[:len(answers)]
    ans_3 = (ans_3_pattern*((len(answers)//len(ans_3_pattern))+1))[:len(answers)]
    
    ans_1_count_correct = 0
    ans_2_count_correct = 0
    ans_3_count_correct = 0
    
    for idx, i in enumerate(answers):
        if ans_1[idx] == i:
            ans_1_count_correct += 1
        if ans_2[idx] == i:
            ans_2_count_correct += 1
        if ans_3[idx] == i:
            ans_3_count_correct += 1
    
    max_score = max([ans_1_count_correct, ans_2_count_correct, ans_3_count_correct])
    for idx, i in enumerate([ans_1_count_correct, ans_2_count_correct, ans_3_count_correct]):
        if i == max_score:
            answer.append(idx+1)
    
    return answer


answers = [1,2,3,4,1,3,3,3,3,2,3,4]
print(solution(answers))