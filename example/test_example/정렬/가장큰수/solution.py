# def sorter(numbers):
    
#     for i in range(len(numbers)-1):
#         for j in range(len(numbers) - i-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

#     return numbers

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: (x*5)[:4], reverse = True)
    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'
    
    return answer


numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]

answer = solution(numbers)
print(answer)