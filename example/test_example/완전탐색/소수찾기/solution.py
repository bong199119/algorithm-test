import itertools
def is_prime_number(number):
    prime_number = False

    if number <= 1:
        return prime_number

    for i in range(1, int(number**0.5)):
        if number%(i+1) == 0:
            return prime_number

    prime_number = True
    return prime_number

def make_permutation(numbers):
    list_numbers_permutation = []
    list_numbers = list(numbers)

    for i in range(len(list_numbers)):
        for k in list(itertools.permutations(list_numbers, i+1)):
            number_new = ''
            for j in k:
                number_new += j
                
            number_new_int = int(number_new)
            if number_new_int not in list_numbers_permutation:
                list_numbers_permutation.append(number_new_int)

    return list_numbers_permutation


def solution(numbers):
    answer = 0
    list_numbers = make_permutation(numbers)
    for number in list_numbers:
        prime_number = is_prime_number(number)
        if prime_number:
            answer += 1

    return answer


# for i in [1, 2, 3, 12, 13, 21, 23, 31, 32, 123, 132, 213, 231, 312, 321]:
#     print(i, is_prime_number(i))

number = "011"
print(make_permutation(number))
print(solution(number))