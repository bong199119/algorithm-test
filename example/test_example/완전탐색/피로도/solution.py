import itertools

def make_permutation(dungeons):
    for i in range(len(dungeons)):
        itertools.permutations()

def canPass_dungeon(list_dungeons):

    return list_dungeons

def solution(k, dungeons):
    answer = -1

    list_dungeons = make_permutation(dungeons)
    list_dungeons_passed = canPass_dungeon(list_dungeons)

    for dungeons_passed in list_dungeons_passed:
        if answer < len(dungeons_passed):
            answer = len(dungeons_passed)

    return answer

