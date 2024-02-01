import urllib.parse

str='hello World 中国'
encode_str=urllib.parse.quote(str)
print(f'URLEncode: ${encode_str}')
# 具体的出错处理 https://docs.python.org/3/library/codecs.html#error-handlers
decode_str=urllib.parse.unquote(encode_str, encoding='utf-8', errors='replace')
