# import time
# start_time = time.time()

# answer = 0
# N = 0
# visited = []


# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt

#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0


# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer

# dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
# k = 80

# answer = solution(k, dungeons)
# print(answer)

# end_time = time.time()
# print(start_time, end_time)
# print('take_time : ', end_time - start_time)


import time
start_time = time.time()

answer = 0
N = 0
visited = []
list_case = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
k = 80

answer = solution(k, dungeons)
print(answer)

end_time = time.time()
print(start_time, end_time)
print('take_time : ', end_time - start_time)
