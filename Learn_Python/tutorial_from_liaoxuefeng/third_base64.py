import base64
print (base64.b64encode(b'binary\x00string'))
print (base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
