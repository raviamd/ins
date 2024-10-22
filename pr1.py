def encrypt(text, s):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)

        # If it's neither, add the character as it is
        else:
            result += char

    return result

# Input the text and shift value
text = input("Enter the text to encrypt: ")
s = int(input("Enter the shift value: "))

# Print the result
print("Text: " + text)
print("Cipher: " + encrypt(text, s))
