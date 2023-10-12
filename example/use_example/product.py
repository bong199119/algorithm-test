from itertools import product

numbers = [1,1,1,1] 
l = [(x,-x)for x in numbers]
print(*l)
print(list(product(*l)))
print(list(product((1,-1),(1,-1),(1,-1),(1,-1))))
print([(x, y, z, k) for x in (1, -1) for y in (1, -1) for z in (1, -1) for k in (1, -1)])