arr = [10, 20, 30]
 
 
def fun():
    global arr
    arr = [20, 30, 40]

print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)