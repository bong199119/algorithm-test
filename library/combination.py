def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result

def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr): 
        for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
            result += [[elem]+P]
              
    return result

def permutations_4(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations_4(array, r-1):
                yield [array[i]] + next



                    