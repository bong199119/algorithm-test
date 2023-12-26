def dfs(i, j, len_rout, maps, list_way):
    list_way_point = [list_way[:]][0]
    print('way', list_way_point)
    map_ele = maps[0]
    print('now', i, j, len_rout)
    print(map_ele[0])
    print(map_ele[1])
    print(map_ele[2])
    print(map_ele[3])
    print(map_ele[4])
    list_way_point.append((i,j))

    if i-1 < -1 or i+1 > len(map_ele) or j-1 < -1 or j+1 > len(map_ele[0]):
        print(map_ele)
        print(i-1, i+1, len(map_ele), j-1,  j+1, len(map_ele[0]))
        print('false')
        return False

    if i == len(map_ele)-1 and j == len(map_ele[0])-1:
        list_for_len_rout.append(len_rout)
        return 

    if map_ele[i][j] == 1:
        map_ele1 = [map_ele[i][:]]
        map_ele1[0][j] = 0
        map_ele[i] = map_ele1[0]
        len_rout += 1

        list_ = [map_ele[:]]
        dfs(i-1, j, len_rout, list_, list_way_point)
        dfs(i+1, j, len_rout, list_, list_way_point)
        dfs(i, j+1, len_rout, list_, list_way_point)
        dfs(i, j-1, len_rout, list_, list_way_point)
    

def solution(maps):
    answer = 0
    i = 0
    j = 0
    len_rout = 0
    idx = 0
    list_way = []

    map_ele = [maps[:]]
    print('map_ele[0][0]', map_ele)
    dfs(i, j, len_rout, map_ele, list_way)
    if list_for_len_rout != []:
        answer = min(list_for_len_rout)
    else:
        answer = -1

    return answer

maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
list_for_len_rout = []
# solution(maps11)
print(solution(maps11))


'''
[1,0,1,1,1]
[1,0,1,0,1]
[1,0,1,1,1]
[1,1,1,0,1]
[0,0,0,0,1]
'''