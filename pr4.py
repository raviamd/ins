from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair (2048 bits)
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Print the keys
print("Private Key:")
print(private_key.decode('ascii'))
print("\nPublic Key:")
print(public_key.decode('ascii'))

# Original and modified documents
original_document = b"This is the original document"
modified_document = b"This is the modified document"

# Create SHA256 hashes of the original and modified documents
original_hash = SHA256.new(original_document)
modified_hash = SHA256.new(modified_document)

# Sign the original document's hash with the private key
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)

# Attempt to verify the signature using the public key and modified document
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(modified_hash, signature)
    print("\nSignature is valid.")
except (ValueError, TypeError):
    print("\nSignature is invalid.")
