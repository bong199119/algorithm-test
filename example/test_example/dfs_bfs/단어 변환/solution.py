def dfs(begin, target, words, list_words):
    for word in words:
        if word not in list_words:
            count = 0
            list_words_new = list_words[:]
            for idx, ele in enumerate(begin):
                if ele == word[idx]:
                    count += 1
            if (count + 1) == len(word):
                begin_new = word
                list_words_new.append(begin_new)
                
                if word == target:
                    list_for_len_rout.append(len(list_words_new))              
                    return 
                
                else:
                    dfs(begin_new, target, words, list_words_new)

def solution(begin, target, words):
    list_words = []
    if target not in words:
        return 0
    dfs(begin, target, words, list_words)
    return min(list_for_len_rout)


# begin = "hit"	
# target = "cog"	
# words = ["hot", "dot", "dog", "lot", "log", "cog"]
# words = ["hot", "dot", "dog", "lot", "log"]


# begin = "aab"
# target = "aba"
# words = ["abb", "aba"]

# list_for_len_rout = []
# print(solution(begin, target, words))
# print(list_for_len_rout)

