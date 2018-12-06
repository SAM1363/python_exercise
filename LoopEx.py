# 1 for x in range(1, 11):
    # print(x)

# 2 for x in range(1, 9):     *

# 3 for x in range(1, 11):
    # if x % 2 != 0:
    #     print(x)     

# 4 x = 5
# for y in range(x):
#     print('*' * x )

# 5 number = int(input("sixe the square? "))
# for x in range(number):
#     print("*" * number)

height = int(input("Height? "))
width = int(input("Width? "))
# for (x, y) in range(height, width):
for x in ragne(height):
    a = " "
    for y in ragne(width):
        if x == 0 or x == height -1 or y == 0 or y == width -1:
                a += "*"
        else:
                a += " "
     print(a)