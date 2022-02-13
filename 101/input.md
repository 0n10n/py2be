```Python
num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
  
# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))
```

类型重塑：

```
## 当然啦，还可以重塑成float，str等
num1 = int(input())
num2 = int(input())

# printing the sum in integer

print(num1 + num2)
```

使用split()一次从input获得多个输入：

```python
# taking two inputs at a time

x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

# taking three inputs at a time

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()
```

使用list 

```
# taking two input at a time

x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()

# taking three input at a time

x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
print()
```

