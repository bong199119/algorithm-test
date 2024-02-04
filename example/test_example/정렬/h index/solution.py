def solution(citations):
    answer = 0
    dict_cont = {}
    list_foranswer = []
    list_count = []
    for i in citations:
        if i not in dict_cont:
            dict_cont[i] = 1
            list_count.append(i)
        else:
            dict_cont[i] += 1

    max_ = max(list_count)
    count_total = 0
    for count in range(max_, -1, -1):
        print(count)
        if count in dict_cont:
            count_total += dict_cont[count]
            if count <= count_total:
                list_foranswer.append(count)
        else:
            if count <= count_total:
                list_foranswer.append(count)

    answer = max(list_foranswer)
    return answer


citations = [3, 0, 6, 1, 5,5,5]
citations = [3, 4]
citations = [0]
answer = solution(citations)
print(answer)