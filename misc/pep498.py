# https://peps.python.org/pep-0498/PEP 498 – Literal String Interpolation
# F/f占位符方式，方便处理非单一值时的场景
msg = ('disk failure', 32)
print(f'出错原因: {msg} ')

# 如果是%格式，就要这么写：
print('error: %s' % (msg,))

# 可以指定格式转换
value = 1234
print(f'input={value:#06x}')

def outer(x):
    def inner():
        x
        return 'x={x}'.format_map(locals())
    return inner
print(outer(42)())