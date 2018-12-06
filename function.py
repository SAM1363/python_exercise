# def f(x):
#     print(x)
# f("hello workld")
# def f(x):
#   return 2 * x + 1
# for  x in range(-3, 5):
#     print("f{x} = {y}".format(x=x, y=f(x)))



# def g(x):
#   return x + 1
# for index in range(-3, 5):
#   print("f({x})={y} \t g({x})={z}".
#   format(
#           x=index, y=f(index), z=g(index)
#        ))

# def myF(a,b,c):
#     print("{} {} {}".format(a=a, b=b, c=c))

# myF(a)
from math import sqrt

# def Q(a, b, c):
#     x1 = -b / (2*a)
#     x2 = sqrt(b**2 - 4*a*c) / (2*a)
#     return (x1 + x2), (x1 - x2)
# print(Q(a=4, b=9, c=7))


# import matplotlib
# matplotlib.use("Agg")
# from matplotlib import pyplot
# f_output = []
# g_output = []
# x_list = list(range(-3, 5))
# for x in x_list:
#   f_output.append(f(x))
#   g_output.append(g(x))
# pyplot.plot(x_list, f_output, x_list, g_output)
# pyplot.savefig('myplot.png')
# pyplot.close() # start a new plot


from turtle import *
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# right(90)
# forward(100)
# mainloop()


# move into position
up()
forward(50)
left(90)
forward(50)
left(90)
down()
# draw the square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

up()
forward(50)
left(90)
forward(50)
left(90)
down()
# draw the square
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)


mainloop()