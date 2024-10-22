from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate RSA key pair (1024 bits)
key_pair = RSA.generate(1024)
pub_key = key_pair.publickey()

# Print the public key components (n and e)
print("Public key (n):", hex(pub_key.n))
print("Public key (e):", hex(pub_key.e))

# Export the public key in PEM format
pub_key_pem = pub_key.exportKey()
print("\nPublic Key (PEM format):")
print(pub_key_pem.decode('ascii'))

# Export the private key in PEM format
priv_key_pem = key_pair.exportKey()
print("\nPrivate Key (PEM format):")
print(priv_key_pem.decode('ascii'))

# Encrypt a message using the public key
msg = b'This is a secret message!'
encryptor = PKCS1_OAEP.new(pub_key)
encrypted_msg = encryptor.encrypt(msg)

# Convert the encrypted message to hex for easy readability
encrypted_hex = binascii.hexlify(encrypted_msg)
print("\nEncrypted message (hex):", encrypted_hex.decode('ascii'))

# Decrypt the message using the private key
decryptor = PKCS1_OAEP.new(key_pair)
decrypted_msg = decryptor.decrypt(encrypted_msg)

# Print the decrypted message
print("\nDecrypted message:", decrypted_msg.decode('ascii'))
