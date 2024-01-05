def add_one(x):  
    return x + 1  
  
# 定义一个数字列表  
numbers = [1, 2, 3, 4, 5]  
  
# 使用 map() 函数将 add_one 函数应用于 numbers 列表中的每个元素  
result = map(add_one, numbers)  
print(type(result))
print(result)
# 使用 list() 将 map 对象转换为列表，以便我们可以打印结果  
result_list = list(result)      
print(type(result_list))

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

##for rr in reversed(Countdown(30)):
    #print(rr)
##for rr in Countdown(30):
    ##print(rr)
print(list(Countdown(30)))