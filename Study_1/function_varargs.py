# 可变参数
def total(a=5, *numbers, **phonebook):
    '''什么都没有啊

    测试一下！
    '''
    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


# 输出默认返回 None
print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
help(total)
