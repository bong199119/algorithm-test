import math
def cal_duedate(progresses, speeds):
    list_due = []
    for idx, progress in enumerate(progresses):
        due = math.ceil((100-progress)/speeds[idx])
        list_due.append(due)
    
    return list_due

def solution(progresses, speeds):
    answer = []
    list_due = cal_duedate(progresses, speeds)
    print(list_due)
    date_ = 0
    answer_tmp = []

    for idx, due_ele in enumerate(list_due):
        if due_ele > date_:
            date_ = due_ele
            answer.append(len(answer_tmp))
            answer_tmp = [due_ele]

        else:
            answer_tmp.append(due_ele)
        
        if idx == len(list_due)-1:
            answer.append(len(answer_tmp))

    return answer[1:]


progresses = [93, 30, 55]
speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

answer = solution(progresses, speeds)
print(answer)
