def solution(nums):
    dict_nums = {}
    answer = 0
    for num in nums:
        if num not in dict_nums:
            dict_nums[num] = 1
        else:
            dict_nums[num] += 1

    kind_nums = int(len(dict_nums.keys()))

    if kind_nums > int(len(nums)/2):
        answer = int(len(nums)/2)

    else:
        answer = kind_nums
        
    return answer


nums = [3,1,2,3]
result = 2
answer = solution(nums)
print(answer)


nums = [3,3,3,2,2,4]
result = 3
answer = solution(nums)
print(answer)

nums = [3,3,3,2,2,2]
result = 2
answer = solution(nums)
print(answer)


