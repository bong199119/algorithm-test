def solution(clothes):
    answer = 0
    dic_cloth = {}
    for cloth in clothes:
        if cloth[1] not in dic_cloth:
            dic_cloth[cloth[1]] = [cloth[0]]
            dic_cloth[cloth[1]].append('none')
        else:
            dic_cloth[cloth[1]].append(cloth[0])

    print(dic_cloth)
        
    return answer


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = solution(clothes)
print(answer)
