# 数据结构
# 列表       Mutable
# 元组 Tuple Immutable  () (2,) (a,b,c)
# 字典
# Sequence
# Set
# import.os
# os.urandom(16)   bytes


def square(x):
    """返回 x 的平方。

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x


if __name__ == '__main__':
    from functools import reduce
    import doctest
    doctest.testmod()

    ss = map(square, [1, 2, 3, 4, 5])
    print(list(ss))
    print(reduce(lambda x, y: x * y, [1, 2, 3]))
