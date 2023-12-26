# 공약수 조합 반환
def get_comdiv(yellow):
    list_comdivs = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow%i == 0:
            list_comdivs.append([i,yellow//i])

    return list_comdivs

# brown에 맞는 공약수 조합 선정
def take_comdiv(brown, list_comdivs):
    outline = list_comdivs[0] * 2 + list_comdivs[1] * 2 + 4
    if brown == outline:
        return True

def solution(brown, yellow):
    answer = []
    comdiv_for_answer = []

    list_comdivs = get_comdiv(yellow)
    for comdiv in list_comdivs:
        if take_comdiv(brown, comdiv) == True:
            comdiv_for_answer = comdiv
    
    if comdiv_for_answer[0] > comdiv_for_answer[1]:
        answer = [comdiv_for_answer[0] + 2, comdiv_for_answer[1] + 2]

    else:
        answer = [comdiv_for_answer[1] + 2, comdiv_for_answer[0] + 2]

    return answer


brown = 24
yellow = 24

answer = solution(brown, yellow)
print(answer)
