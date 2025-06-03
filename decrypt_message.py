from Crypto.Util.number import long_to_bytes
import json
import os

# Prompt for private key file
privkey_file = input("Enter your private key file (e.g., my_private_key.json): ").strip()
if not privkey_file:
    privkey_file = "my_private_key.json"

# Load your private key
if not os.path.isfile(privkey_file):
    print(f"Error: File '{privkey_file}' not found.")
    exit(1)

with open(privkey_file, "r") as f:
    my_keys = json.load(f)

N = my_keys["N"]
d = my_keys["d"]

# Prompt for encrypted message file
cipher_file = input("Enter encrypted message file (e.g., encrypted_message.txt): ").strip()
if not cipher_file:
    cipher_file = "encrypted_message.txt"

# Load encrypted message
if not os.path.isfile(cipher_file):
    print(f"Error: File '{cipher_file}' not found.")
    exit(1)

with open(cipher_file, "r") as f:
    cipher = int(f.read().strip())

# Decrypt
plain_int = pow(cipher, d, N)
message = long_to_bytes(plain_int).decode('utf-8', errors='ignore')

print("Decrypted message:", message)
