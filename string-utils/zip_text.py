
import zlib
import base64

input_text=input("input string: " )
text_compressed=base64.b64encode(zlib.compress(input_text.encode('utf-8')))
print(str(text_compressed))
