# # def solution(maps):
# #     new_map = maps[:3]
# #     print('new_map', new_map)
# #     maps[2][4] = 0
# #     print('new_map', new_map)

# # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# # list_for_len_rout = []
# # solution(maps)
# # print(maps)


# dict_test = {}

# maps1 = [1,2,3]
# maps2 = [7,4,5]

# dict_test['a'] = list(maps1)
# dict_test['b'] = maps2[:]

# list_t1 = [maps1]
# list_t2 = [list(maps1)]
# list_t3 = [maps1[:]]

# # print(maps1)
# # print(list_t1)
# # print(list_t2)
# # print(list_t3)
# # print()

# # # print(dict_test)

# # maps1[0] = 10
# # maps2[0] = 10

# # # print(dict_test)

# # print(maps1)
# # print(list_t1)
# # print(list_t2)
# # print(list_t3)
# # print([maps1[:]])
# # print(list_t2[0])
# # print(list_t3[0])

# # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# # new_map = maps[:]
# # new_map2 = list(maps)
# # print('new_map', new_map)
# # print('new_map2', new_map2)
# # maps[2][4] = 0
# # print('new_map', new_map)
# # print('new_map2', new_map2)

# list_t2 = [1,2,3]

# def get_map(map1):
#     map1[0][0] = 1111
#     map_k = [map1[:]]
#     return map_k


# def get_map1(map_):
#     map_[0][0] = 2222

# list_1 = [list_t2[:]]
# list_2 = [list_t2[:]]

# get_map(list_1)
# print(list_t2)
# print(list_1)
# print(list_2)
# print()

# get_map1(list_1)
# print(list_t2)
# print(list_1)
# print(list_2)



# maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# num = 0
# dict_for_maps = {}
# list_for_len_rout = []


# maps1 = [maps11[:]]
# print(maps1)
# print(maps11)
# print('aaaaaaaaaaaaaaaaaaa')
# test1 = get_map(maps1)
# print(test1)
# print(maps1)
# print(maps11)
# get_map1(test1)
# print(test1)
# print(maps1)
# print(maps11)
# def dfs1(i, j, len_rout, kmaps):
#     map_ele = kmaps[0]
#     print('map_ele[i][j]', map_ele[i][j])
#     if map_ele[i][j] == 1:
#         map_ele[i][j] = 0
#         list_ = [map_ele[:]]
#         dfs(i-1, j, len_rout, list_)


# def dfs(i, j, len_rout, kmaps):
#     map_ele = kmaps[0]
#     print('map_ele[i][j]', map_ele[i][j])
#     if map_ele[i][j] == 1:
#         map_ele[i][j] = 0
#         list_ = [map_ele[:]]
#         dfs1(i-1, j, len_rout, list_)
    
# def solution(maps):
#     i = 0
#     j = 0
#     len_rout = 0
#     map_ele = [maps[0][:]]
#     map_ele[0][0][0] = 3
#     map_ele[0][0] = [1,2,3,]
#     print(map_ele)
#     print('maps1', maps1)
#     print('maps11',maps11)
#     dfs(i, j, len_rout, map_ele)

# maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# num = 0
# dict_for_maps = {}
# list_for_len_rout = []


# maps1 = [maps11[:]]
# print(maps1)
# print(maps11)
# print('aaaaaaaaaaaaaaaaaaa')
# solution(maps1)
# print('maps1', maps1)
# print('maps11',maps11)




# maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps1 = [maps11[:]]

# maps1[0][0][0] = 3
# print(maps1)
# print(maps11)

# maps11 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps1[0][0] = [1,2,3,]
# print(maps1)
# print(maps11)


maps112 = [1,2,3]
maps113 = [3,3,3,]
maps114 = [56,6,6,]

list_1 = [maps112, maps113, maps114]
list_2 = [[maps112[:]][0], [maps113[:]][0], [maps114[:]][0]]

print(list_1)
print(list_2)

maps112[0] = 11

print(list_1)
print(list_2)

list_3 = [list_1, list_2]
list_4 = [[list_1[:]][0], [list_2[:]][0]]

print(list_3)
print(list_4)

maps112[0] = 112

print(list_3)
print(list_4)

# list_4[0][2][1] = 777
list_4[1][2][1] = 777
print(list_3)
print(list_4)
print(maps114)

list7 = [list_4[:][:][:]]
print(list7)

list_4[1][2][1] = 778
print(list_3)
print(list_4)
print(maps114)
print(list7)
