# https://peps.python.org/pep-0498/PEP 498 – Literal String Interpolation
# F/f占位符方式，方便处理非单一值时的场景
msg = ('disk failure', 32)
print(f'出错原因: {msg} ')

# 如果是%格式，就要这么写：
print('error: %s' % (msg,))

# 可以指定格式转换
value = 1234
print(f'input={value:#06x}')

# 引号的处理，使用不同形式的引号：
print(f'{"quoted string"}')

# 怎么转义大括号本身,使用双层括号：
print(f'{{ {4*10} }}')

# 可以执行代码/表达式
# f'abc{expr1:spec1}{expr2!r:spec2}def{expr3}ghi'  等价于：
# 'abc' + format(expr1, spec1) + format(repr(expr2), spec2) + 'def' + format(expr3) + 'ghi'
# 例子：
def foo():
  return 20

result=f'{foo()}' # 相当于：result=str(foo())
print(result)
