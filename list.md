# Python – List Comprehension



A Python list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element in the [Python list](https://www.geeksforgeeks.org/python-list/). 

## Python List Comprehension Syntax

> ***\*Syntax:\**** newList ***\*=\**** ***\*[\**** expression(element) ***\*for\**** element ***\*in\**** oldList ***\*if\**** condition ***\*]\**** 
>
> 
>
> ***\*Parameter:\****
>
> - **`\**expression\**`**: Represents the operation you want to execute on every item within the iterable.
> - **`\**element\**`**: The term “variable” refers to each value taken from the iterable.
> - **`\**iterable\**`**: specify the sequence of elements you want to iterate through.(e.g., a list, tuple, or string).
> - **`\**condition\**`**: (Optional) A filter helps decide whether or not an element should be added to the new list.
>
> ***\*Return:\******The return value of a list comprehension is a new list containing the modified elements that satisfy the given criteria.**
>
> Python List comprehension provides a much more short syntax for creating a new list based on the values of an existing list.
>


## List Comprehension in Python Example

Here is an example of using list comprehension to find the square of the number in [Python.](https://www.geeksforgeeks.org/python-programming-language/)

- Python3

```
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)
```

***\*Output\****

```
[1, 4, 9, 16, 25]
```

### Iteration with List Comprehension

In this example, we are assigning 1, 2, and 3 to the list and we are printing the list using List Comprehension.

- Python3

```
# Using list comprehension to iterate through loop
List = [character for character in [1, 2, 3]]
 
# Displaying list
print(List)
```

***\*Output\****

```
[1, 2, 3]
```

### Even list using List Comprehension

In this example, we are printing the even numbers from 0 to 10 using List Comprehension.

- Python3

```
list = [i for i in range(11) if i % 2 == 0]
print(list)
```

***\*Output\****

```
[0, 2, 4, 6, 8, 10]
```

### Matrix using List Comprehension

In this example, we are assigning integers 0 to 2 to 3 rows of the matrix and printing it using List Comprehension.

- Python3

```
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
```

***\*Output\****

```
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

## List Comprehensions vs For Loop

There are various ways to iterate through a list. However, the most common approach is to use the [**for** loop](https://www.geeksforgeeks.org/python-for-loops/). Let us look at the below example:

- Python3

```
# Empty list
List = []
 
# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
    List.append(character)
 
# Display list
print(List)
```

***\*Output\****

```
['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's', '!']
```

Above is the implementation of the traditional approach to iterate through a list, string, tuple, etc. Now, list comprehension in Python does the same task and also makes the program more simple. 

List Comprehensions translate the traditional iteration approach using [for loop](https://www.geeksforgeeks.org/python-for-loops/) into a simple formula hence making them easy to use. Below is the approach to iterate through a list, string, tuple, etc. using list comprehension in Python.

- Python3

```
# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']
 
# Displaying list
print(List)
```

***\*Output\****

```
['G', 'e', 'e', 'k', 's', ' ', '4', ' ', 'G', 'e', 'e', 'k', 's', '!']
```

## Time Analysis in List Comprehensions and Loop

The list comprehensions in Python are more efficient both computationally and in terms of coding space and time than a for a loop. Typically, they are written in a single line of code. The below program depicts the difference between loops and list comprehension based on performance.

- Python3

```
# Import required module
import time
 
 
# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result
 
 
# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]
 
 
# Driver Code
 
# Calculate time taken by for_loop()
begin = time.time()
for_loop(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for_loop:', round(end-begin, 2))
 
# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10**6)
end = time.time()
 
# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end-begin, 2))
```

***\*Output\****

```
Time taken for_loop: 0.39
Time taken for list_comprehension: 0.35
```

From the above program, we can see list comprehensions are quite faster than for loop.

## Nested List Comprehensions

[Nested List Comprehensions](https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/) are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops. Below is the program which implements nested loop:

- Python3

```
matrix = []
 
for i in range(3):
 
    # Append an empty sublist inside the list
    matrix.append([])
 
    for j in range(5):
        matrix[i].append(j)
 
print(matrix)
```

***\*Output\****

```
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

Now by using nested list comprehensions, the same output can be generated in fewer lines of code.

- Python3

```
# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
 
print(matrix)
```

***\*Output\****

```
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

## List Comprehensions and Lambda

[Lambda Expressions](https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/) are nothing but shorthand representations of Python functions. Using list comprehensions with lambda creates an efficient combination. Let us look at the below examples:

In this example, we are inserting numbers from 10 to 50 in the list and printing it.

- Python3

```
# using lambda to print table of 10 
numbers = []
 
for i in range(1, 6):
    numbers.append(i*10)
 
print(numbers)
```

***\*Output\****

```
[10, 20, 30, 40, 50]
```

Here, we have used for loop to print a table of 10.

- Python3

```
numbers = [i*10 for i in range(1, 6)]
 
print(numbers)
```

***\*Output\****

```
[10, 20, 30, 40, 50]
```

 Now here, we have used only list comprehension to display a table of 10.

- Python3

```
# using lambda to print table of 10
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
 
print(numbers)
```

***\*Output\****

```
[10, 20, 30, 40, 50]
```

Finally, we use lambda + list comprehension to display the table of 10. This combination is very useful to get efficient solutions in fewer lines of code for complex problems.

## Conditionals in List Comprehension

We can also add conditional statements to the list comprehension. We can create a list using [range(),](https://www.geeksforgeeks.org/python-range-function/) [operators](https://www.geeksforgeeks.org/python-operators/), etc. and cal also apply some conditions to the list using the [if statement](https://www.geeksforgeeks.org/python-if-else/).

***\*Key Points\****

- Comprehension of the list is an effective means of describing and constructing lists based on current lists.
- Generally, list comprehension is lightweight and simpler than standard list formation functions and loops.
- We should not write long codes for list comprehensions in order to ensure user-friendly code.
- Every comprehension of the list can be rewritten in for loop, but in the context of list interpretation, every for loop can not be rewritten.

Below are some examples which depict the use of list comprehensions rather than the traditional approach to iterate through iterable:

### Python List Comprehension using If-else.

In the example,  we are checking that from 0 to 7 if the number is even then insert ***\*Even Number\**** to the list else insert ***\*Odd Number\**** to the list.

- Python3

```
lis = ["Even number" if i % 2 == 0
       else "Odd number" for i in range(8)]
print(lis)
```

***\*Output\****

```
['Even number', 'Odd number', 'Even number', 'Odd number', 
'Even number', 'Odd number', 'Even number', 'Odd number']
```

### Nested IF with List Comprehension

In this example, we are inserting numbers in the list which is a multiple of 10 to 100, and printing it.

- Python3

```
lis = [num for num in range(100) 
       if num % 5 == 0 if num % 10 == 0]
print(lis)
```

***\*Output\****

```
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

### Display a square of numbers from 1 to 10

In this example, we are inserting a square from 1 to 10 to list and printing the list.

- Python3

```
# Getting square of number from 1 to 10
squares = [n**2 for n in range(1, 11)]
 
# Display square of even numbers
print(squares)
```

***\*Output\****

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Display Transpose of 2D- Matrix

In this example, we are making a transpose of the matrix using list comprehension.

- Python3

```
# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
 
# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]
 
print(trans)
```

***\*Output\****

```
[[10, 40, 70], [20, 50, 80], [30, 60, 90]]
```

### Toggle the case of each character in a String

In this example, we toggle the case of each character in a given string using the XOR operator with 32 and store the result in a list.

- Python3

```
# Initializing string
string = 'Geeks4Geeks'
 
# Toggle case of each character
List = list(map(lambda i: chr(ord(i) ^ 32), string))
 
# Display list
print(List)
```

***\*Output\****

```
['g', 'E', 'E', 'K', 'S', '\x14', 'g', 'E', 'E', 'K', 'S']
```

### Reverse each string in a Tuple

In this example, we are reversing strings in for loop and inserting them into the list, and printing the list.

- Python3

```
# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
 
# Display list
print(List)
```

***\*Output\****

```
['skeeG', 'rof', 'skeeG']
```

### Creating a list of Tuples from two separate Lists

In this example, we have created two lists of ***\*names and ages.\**** We are using ***\*zip()\**** in list comprehension and we are inserting the name and age as a tuple to list. Finally, we are printing the list of tuples.

- Python3

```
names = ["G", "G", "g"]
ages = [25, 30, 35]
person_tuples = [(name, age) for name, age in zip(names, ages)]
print(person_tuples)
```

***\*Output:\****

```
[('G', 25), ('G', 30), ('g', 35)]
```

### Display the sum of digits of all the odd elements in a list.

In this example, We have created a list and we are finding the digit sum of every odd element in the list.

- Python3

```
# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
 
 
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
 
# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
 
# Displaying new list
print(newList)
```

***\*Output\****

```
[16, 3, 18, 18]
```

### ***\*Advantages of List Comprehension\****

- More time-efficient and space-efficient than loops.
- Require fewer lines of code.
- Transforms iterative statement into a formula.

Don't miss your chance to ride the wave of the data revolution! Every industry is scaling new heights by tapping into the power of data. Sharpen your skills, become a part of the hottest trend in the 21st century.
Dive into the future of technology - explore the [Complete Machine Learning and Data Science Program](https://www.geeksforgeeks.org/python-list-comprehension/www.geeksforgeeks.org/courses/data-science-live?utm_source=geeksforgeeks&utm_medium=article_bottom_text&utm_campaign=courses) by GeeksforGeeks and stay ahead of the curve.

Last Updated : 18 Aug, 2023

