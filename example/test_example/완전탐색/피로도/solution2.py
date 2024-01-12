import time
start_time = time.time()
list_totalcount = []

def dfs(dungeons, k, list_visit):
    for idx, dungeon in enumerate(dungeons):
        if dungeon[0] <= k and list_visit[idx] == 0:
            k_new = k - dungeon[1]
            list_visit[idx] = 1
            dfs(dungeons, k_new, list_visit)
            list_visit[idx] = 0

        else:
            list_totalcount.append(list_visit.count(1))


def solution(k, dungeons):
    answer = -1
    list_visit = [0] * len(dungeons)

    dfs(dungeons, k, list_visit)
    answer = max(list_totalcount)

    return answer

dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
k = 80

answer = solution(k, dungeons)
print(answer)

end_time = time.time()
print(start_time, end_time)
print('take_time : ', end_time - start_time)
