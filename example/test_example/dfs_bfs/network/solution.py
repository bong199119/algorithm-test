def dfs(raw_idx, computers):
    global is_network

    for colum_idx, ele in enumerate(computers[raw_idx]):
        if colum_idx >= raw_idx:
            if ele == 1:
                for raw_idx_n in range(colum_idx + 1):
                    if computers[raw_idx_n][colum_idx] == 1:
                        is_network += 1
                        computers[raw_idx][colum_idx] = 0
                        dfs(raw_idx_n, computers)

def solution(n, computers):
    global is_network
    
    total_net = 0
    for raw_idx in range(len(computers)):
        is_network = 0
        dfs(raw_idx, computers)
        for i in range(len(computers)):
            print(computers[i])
        print()

        if is_network > 0:
            total_net += 1
            
    answer = total_net        
    return answer

computers = [
    [1,0,1],
    [0,1,0],
    [1,0,1],
]
n = 3

computers = [
    [1,0,0,0,1],
    [0,1,0,0,0],
    [0,0,1,0,1],
    [0,0,0,1,0],
    [1,0,1,0,1],
]
n = 5

computers = [
    [1,1,0,0,1],
    [1,1,0,0,0],
    [0,0,1,1,1],
    [0,0,1,1,0],
    [1,0,1,0,1],
]
n = 5

is_network = 0
print('solution : ',solution(n, computers))


