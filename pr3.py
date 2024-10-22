import hashlib
str_input = input("Enter the value to encode: ")
hash_object = hashlib.sha1(str_input.encode())
hex_result = hash_object.hexdigest()
print("The hexadecimal equivalent of SHA1 is:", hex_result)
