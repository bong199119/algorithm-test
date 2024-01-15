n = 3
# list_test = [1,2,3,4,5]
# list_test.pop(1)
# print(list_test)
# print([0]*n)
# print([[0]*n]*9)


map_wires = [[0]*n]*n
map_wires1 = [[0,0,0],[0,0,0],[0,0,0]]
map_wires2 = [[0]*n, [0]*n, [0]*n]
print(map_wires)
print(map_wires2)

map_wires[1][2] = 1
for i in map_wires:
    print(i)

print()
map_wires1[1][2] = 1
for i in map_wires1:
    print(i)

print()
map_wires2[1][2] = 1
for i in map_wires2:
    print(i)