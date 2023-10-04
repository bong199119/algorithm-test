from itertools import permutations, product

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

arr_sign = ['+','-']
arr = [1,2,3,1]
len_arr = len(arr)
target_number = 5

permutation_arr_sign = list(product(arr_sign, repeat=len_arr))
combinations_arr = gen_combinations(arr,len_arr)

print(permutation_arr_sign)
print(combinations_arr)

list_solution_containner = []
sign_ele_number = 0

for arr_ in combinations_arr:
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

        if cal == target_number:
            print(cal)
            print(list_solution_containner_tmp)
            list_solution_containner.append(list_solution_containner_tmp)
            

print(len(list_solution_containner))
print(list_solution_containner)

                