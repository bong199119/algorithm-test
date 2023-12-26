def test(matrix):
    global num
    num+=1
    for idx, matrix_ele in enumerate(matrix):
        if 4 in matrix_ele:
            matrix[idx] = []

def test2():
    global num
    num = 13
    num+=1



matrix = [[1,2,3], [2,2,2], [2,2,4]]
num = 0
test(matrix)
test2()
print(num)
print(matrix)



for i in range(1):
    print('a')