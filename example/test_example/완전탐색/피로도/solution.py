import itertools
import time

start_time = time.time()
def make_permutation(dungeons):
    list_dungeons = []
    for i in range(len(dungeons)):
        list_dungeons += list(itertools.permutations(dungeons, i + 1))
        # print(list_dungeons)

    return list_dungeons

def canPass_dungeon(k, list_dungeons):
    list_dungeons_passed = []

    for dungeons in list_dungeons:
        k_forpass = k
        pass_num = 0
        for dungeon in dungeons:
            if k_forpass >= dungeon[0]:
                k_forpass -= dungeon[1] 
                if k_forpass >= 0:
                    pass_num += 1
        if pass_num == len(dungeons):
            list_dungeons_passed.append(dungeons)

    return list_dungeons_passed

def solution(k, dungeons):
    answer = -1
    global list_dungeons_passed

    list_dungeons = make_permutation(dungeons)
    list_dungeons_passed = canPass_dungeon(k, list_dungeons)

    for dungeons_passed in list_dungeons_passed:
        if answer < len(dungeons_passed):
            answer = len(dungeons_passed)
            list_dungeons_passed = dungeons_passed

    return answer


dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
k = 80
list_dungeons_passed = []

answer = solution(k, dungeons)
print(answer)

end_time = time.time()
print(start_time, end_time)
print('take_time : ', end_time - start_time)
print(list_dungeons_passed)
