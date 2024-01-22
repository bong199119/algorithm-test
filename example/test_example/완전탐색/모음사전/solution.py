import itertools

def make_permutation(list_words):
    list_words_per = []
    for idx in range(len(list_words)):
        list_words_per += list(itertools.product(list_words, repeat = idx+1))

    return list_words_per

def find_answer(list_words_per, word):
    for idx, word_per in enumerate(list_words_per):
        word_ = ''
        for word_ele in word_per:
            word_ += word_ele

        if word == word_:
            answer = idx+1

    return answer

def solution(word):
    answer = 0
    list_words_per = make_permutation(list_words)
    list_words_per.sort()
    answer = find_answer(list_words_per, word)

    return answer

word = "AAAAE"
list_words = ['A', 'E', 'I', 'O', 'U']
answer = solution(word)
print(answer)
