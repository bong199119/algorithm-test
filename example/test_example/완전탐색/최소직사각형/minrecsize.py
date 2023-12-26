def solution(sizes):
    answer = 0
    max_size = 0
    max_size_otherside = 0
    list_max_size = []
    list_max_size_otherside = []
    
    for size in sizes:
        list_max_size_otherside.append(min(size))
        list_max_size.append(max(size))
                
    max_size = max(list_max_size)
    max_size_otherside = max(list_max_size_otherside)
    answer = max_size*max_size_otherside
    return answer