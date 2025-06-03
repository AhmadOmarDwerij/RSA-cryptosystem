from Crypto.Util.number import bytes_to_long
import json

# Read friend's public key
public_file = input("Enter friend's public key file name (e.g., friend_public_key.json): ").strip()
if not public_file:
    public_file = "friend_public_key.json"

try:
    with open(public_file, "r") as f:
        pubkey = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{public_file}' not found.")
    exit(1)

N = pubkey["N"]
e = pubkey["e"]

# Message to encrypt
message = input("Enter message to encrypt: ").strip()
m_int = bytes_to_long(message.encode('utf-8'))

# Encrypt
cipher = pow(m_int, e, N)
print("Encrypted message:", cipher)

# Ask user for filename to save encrypted message
output_file = input("Enter filename to save encrypted message (e.g., encrypted.txt): ").strip()
if not output_file:
    output_file = "encrypted_message.txt"

with open(output_file, "w") as f:
    f.write(str(cipher))

print(f"[+] Encrypted message saved to '{output_file}'")
