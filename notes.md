## 1，星号的含义

在Python中，星号（*）符号具有多种含义，根据上下文的不同可以有不同的用途。以下是一些常见的用法：

1. 解包（Unpacking）：星号可以用于解包序列（如列表或元组）中的元素。当应用于序列时，星号将序列拆分为单独的元素。例如：

```
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 输出: 1
print(b)  # 输出: [2, 3, 4]
print(c)  # 输出: 5
```

在上面的例子中，星号将列表中的中间元素（2、3、4）打包为一个新的列表`b`，而首尾的元素则分别赋值给`a`和`c`。

1. 可变数量的参数（Arbitrary Arguments）：星号可以用于在函数定义中接受可变数量的参数。这些参数被视为一个元组。例如：

```
def foo(*args):
    for arg in args:
        print(arg)

foo(1, 2, 3)  # 输出: 1 2 3
```

在这个例子中，`foo`函数接受任意数量的参数，并将它们打印出来。

1. 可变数量的关键字参数（Arbitrary Keyword Arguments）：双星号（**）可以用于接受可变数量的关键字参数。这些参数被视为一个字典。例如：

```
def bar(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

bar(name='Alice', age=25)  # 输出: name Alice  age 25
```

在这个例子中，`bar`函数接受任意数量的关键字参数，并将它们打印出来。

1. 扩展迭代器（Extended Iterable Unpacking）：星号还可以用于扩展迭代器的元素。例如：

```
first, *middle, last = 'Hello'
print(first)   # 输出: H
print(middle)  # 输出: ['e', 'l', 'l']
print(last)    # 输出: o
```

在这个例子中，星号将字符串的中间字符打包为一个新的列表`middle`，而首尾的字符则分别赋值给`first`和`last`。

这些只是星号在Python中的一些常见用法，具体使用取决于上下文和特定的编程需求。

## 2，把函数作为另一个函数的参数

```
def perform(fun, *args):
    fun(*args)

def action1(args):
    # something

def action2(args):
    # something

perform(action1)
perform(action2, p)
perform(action3, p, r)
```

1. Python closures 用作回调函数，它们提供了某种程度的数据隐藏。可以帮助减少全局变量的使用。
2. When we have few functions in our code, 代码里用到的函数比较少时，closures 函数有助于使程序更精简高效。 如果函数多，那就还是用 class (OOP) 的面向对象编程吧。        
3. 我们经常有些放在全局的变量，并没有很多函数要用到它们。与其放在全局，不如放在closure函数。它们可以在外层函数里定义，在内层函数里使用。
4. Python 的 class 一定需要一个 __init__ 方法。如果除了init方法外，只有一个别的method，那更优雅的做法是使用 closure 函数而不是class。这种做法可以提供代码的可读性，减少程序员的工作量。