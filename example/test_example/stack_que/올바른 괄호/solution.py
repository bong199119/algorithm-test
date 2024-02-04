def solution(s):
    answer = True
    left_parenthesis = '('
    right_parenthesis = ')'

    list_tmp = []

    for idx, s_ele in enumerate(s):
        if s_ele == left_parenthesis:
            list_tmp.append(s_ele)

        # 중간에 문법오류난 경우
        elif s_ele == right_parenthesis:
            if len(list_tmp) == 0:
                answer = False
                return answer
            else:
                list_tmp.pop()             
    
    # left_parenthesis가 더 많은 경우
    if len(list_tmp) != 0:
        answer = False
        return answer

    return answer

s = "()()"
# s = "(())()"
# s = ")()("
# s = "(()("

answer = solution(s)
print(answer)
