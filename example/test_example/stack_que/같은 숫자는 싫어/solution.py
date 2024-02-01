def solution(arr):
    answer = []
    before = None
    for arr_ele in arr:
        if before != arr_ele:
            before = arr_ele
            answer.append(arr_ele)
    return answer