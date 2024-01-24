def solution(phone_book):
    answer = True
    phone_book.sort()
    for idx, num in enumerate(phone_book[:-1]):
        if num == phone_book[idx+1][:len(num)]:
            answer = False
        
    return answer

def solution(phone_book):
    answer = True
    dic_phone = {}
    for num in phone_book:
        dic_phone[num] = 1
    
    for num in phone_book:
        tmp = ''
        for num_ele in num:
            tmp += num_ele
            if tmp in dic_phone and tmp != num:
                answer = False

    return answer

phone_book = ["119", "97674223", "1195524421"]
return_ = False

answer = solution(phone_book)
print(answer)

phone_book = ["123","456","789"]
return_ = True

answer = solution(phone_book)
print(answer)

phone_book = ["12","123","1235","567","88"]
return_ = False

answer = solution(phone_book)
print(answer)