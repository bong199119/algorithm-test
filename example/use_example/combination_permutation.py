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

from itertools import permutations, product

arr_sign = ['+','-']
arr = [1,2,3]
len_arr = len(arr)
target_number = 5

permutation_arr_sign = list(product(arr_sign, repeat=len_arr))
premutation_arr = gen_permutations(arr,len_arr)

list_solution_containner = []
sign_ele_number = 0

for arr_ in premutation_arr:
    for sign_ in permutation_arr_sign:
        cal = 0
        list_solution_containner_tmp = []
        for idx, arr_ele in enumerate(arr_):
            if sign_[idx] == '+':
                sign_ele_number = 1
            elif sign_[idx] == '-':
                sign_ele_number = -1

            cal += sign_ele_number*arr_ele
            list_solution_containner_tmp.append(sign_[idx])
            list_solution_containner_tmp.append(arr_ele)

            if cal > target_number:
                break

            elif cal == target_number:
                if list_solution_containner_tmp not in list_solution_containner:
                    list_solution_containner.append(list_solution_containner_tmp)
            

print(len(list_solution_containner))
print(list_solution_containner)

                