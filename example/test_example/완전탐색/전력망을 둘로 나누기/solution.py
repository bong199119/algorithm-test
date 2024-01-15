def dfs(map_wires, idx_raw, list_tmp_net, list_total_net):

    for idx_col in range(len(map_wires[idx_raw])):
        if map_wires[idx_raw][idx_col] == 1:
            map_wires[idx_raw][idx_col] = 0

            if idx_col+1 not in list_tmp_net:
                list_tmp_net.append(idx_col+1)

            if idx_col != idx_raw:
                dfs(map_wires, idx_col, list_tmp_net, list_total_net)

def make_map(n, wires):
    map_wires = []
    for i in range(n):
        map_wires.append([0]*n)
        map_wires[i][i] = 1

    for wire in wires:
        map_wires[wire[0]-1][wire[1]-1] = 1
        map_wires[wire[1]-1][wire[0]-1] = 1

    return map_wires

def cal_map(map_wires):
    abs_map = 0
    list_total_net = []
    
    for idx_raw in range(len(map_wires)):
        list_tmp_net = []
        dfs(map_wires, idx_raw, list_tmp_net, list_total_net)
        if list_tmp_net != []:
            list_total_net.append(list_tmp_net)
    
    abs_map = abs(len(list_total_net[0]) - len(list_total_net[1]))
    return abs_map

def solution(n, wires):
    answer = -1
    list_abs_tree = []

    for idx, wire in enumerate(wires):
        wires_ = wires[:]
        wires_.pop(idx)
        map_wires = make_map(n, wires_)
        abs_map = cal_map(map_wires)
        list_abs_tree.append(abs_map)

    answer = min(list_abs_tree)
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[7,8],[7,9]]

answer = solution(n, wires)
print(answer)
