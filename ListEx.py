# L1 = [1, 4, 6, 3]
# L2 = [8, 6, 3, 9]
# L3 = []
# 1 print(sum(L1))
# 2 print(max(L1))   
# 3 print(min(L1))
# 4 for x in L1:
#     if x % 2 == 0:
#         print(x)

# 5 for x in L1:
#     if x > 0:
#         print(x)

# 6 for x in L1:
#     if x > 0:
#         L3.append(x)
# print(L3)   

# 7 for x in L1:
#     y = 0
#     for z in L2:
#         y += x * z
#         print(x, z, y)
#     L3.append(y)    
# print(L3)

# for (x, y) in zip(L1, L2):
#     z = x * y
#     L3.append(z)
# print(L3) 

# 9 a = [[4,7], [3,5]]
# b = [[1,3], [9,2]]
# c = [[0,0], [0,0]]
# for x in range(len(a)):
#     for y in range(len(a[0])):
#         c[x][y] = a[x][y] + b[x][y]

# for result in c:
#     print(result)    


# 10 a = [[4,7,3], [3,5,2]]
# b = [[1,3,5], [9,2,7]]

# result = [list(map(sum, zip(*t))) for t in zip(a, b)]
# print(result)

# 11 a = 1,2,3,2,1,6,5,8
# b = 1,4,3,6,7,8,5,4
# print(list(set(a+b)))