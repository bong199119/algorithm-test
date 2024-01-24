def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    # for num in phone_book:
    #     for num_com in phone_book:
    #         if num != num_com and num == num_com[:len(num)]:
    #             answer = False

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