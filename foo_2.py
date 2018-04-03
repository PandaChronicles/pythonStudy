# -*- coding: utf-8 -*-
# or and not
# | ^ &
# << >>
# + -
# * / // %
# +x, -x, ~x
# **
print("test!" * 2)
x = 50


def func():
    global x
    x += 1
    print("Change global x to", x)


func()
print("x is {} now".format(x))

# 参数，关键字参数，可变参数
