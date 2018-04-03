# -*- coding: utf-8 -*-

# Alt+Shift+F

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0 / 3), end='')
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^13}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

name = 'Swaroop'
bookName = 'A Byte of Python'

print('{name} wrote {book}'.format(name=name, book=bookName))

str = "\
這是一個字符串，\
这是一个字符串"

# 原始字符串 r
raw = r'\\\\n""""""nnn\n\n]n;'

print(raw)

i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)
