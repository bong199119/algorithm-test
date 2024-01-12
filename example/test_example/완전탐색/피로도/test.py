dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
# list_1 = [80,20,10,50,60]

# list_1_1 = list_1[:]
# list_1_2 = list_1
# list_1_1[0] = 100
# print(list_1)
# print(list_1_1)

# list_1_2[1] = 1000
# print(list_1)
# print(list_1_1)
# print(list_1_2)

# dungeons_1 = dungeons
# dungeons_2 = dungeons
# dungeons_3 = dungeons[:]

# print(dungeons[:])
# dungeons_1[0] = 11

# print(dungeons_1)
# print(dungeons_2)
# print(dungeons_3)

# dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
# dungeons_1 = dungeons
# dungeons_2 = dungeons
# dungeons_3 = dungeons[:]

# dungeons_1[0][0] = 11

# print('dungeons_1', dungeons_1)
# print('dungeons_2', dungeons_2)
# print('dungeons_3', dungeons_3)

dungeons = [[80,20],[50,40],[30,10],[80,20],[50,40],[10,40],[10,40],[10,40]]
dungeons_1 = dungeons
dungeons_2 = dungeons
dungeons_3 = dungeons[:]
dungeons_4 = dungeons[:][:]
dungeons_1[0] = dungeons[0][:]
print(dungeons_3)

dungeons_2[0][0] = 11
dungeons[0][0] = 1
dungeons_3[0][0] = 22

print('dungeons_1', dungeons_1)
print('dungeons_2', dungeons_2)
print('dungeons_3', dungeons_3)
print('dungeons_4', dungeons_4)


list_1 = [80,20,10,50,60]
print(list_1.count(0))