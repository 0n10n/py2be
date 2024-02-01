from urllib.parse import unquote  

user_input = input("请输入一串字符串：")
bytes_sequence = bytes.fromhex(user_input)  # 将十六进制字符串转换为字节序列  
print(bytes_sequence)  # 输出：b'Hello World'
#print(decoded_string)
string = bytes_sequence.decode('utf-8', errors='ignore')
print(string)

