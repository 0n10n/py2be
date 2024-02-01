from urllib.parse import unquote  

user_input = input("请输入一串字符串：")

result = ""  
  
for i in range(0, len(user_input), 2):  
    result += "%" + user_input[i:i+2]

print(result)
decoded_string = unquote(result)  
#print(decoded_string)

