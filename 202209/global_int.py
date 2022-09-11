def f():
    global s
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s) 
  
# Global Scope
s = "Python is great!" 
f()
#print(s)