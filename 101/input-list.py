#!"C:\Python310\python.exe" 

#x, y=map(int, input("Enter numbers").split())
#print(x)
#print(y)


# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)