from Crypto.Util.number import getPrime, inverse
import json

valid_sizes = [128, 256, 512, 1024, 2048]

while True:
    try:
        key_size = int(input(f"Enter key size in bits {valid_sizes}: "))
        if key_size not in valid_sizes:
            print(f"Please choose a key size from the list: {valid_sizes}")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Ask user for file name base
file_base = input("Enter a base name for the key files (e.g., 'mykey'): ").strip()
if not file_base:
    file_base = "mykey"

def generate_keys(bits):
    e = 65537
    p = getPrime(bits // 2)
    q = getPrime(bits // 2)
    while p == q:
        q = getPrime(bits // 2)

    N = p * q
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

    return {"N": N, "e": e, "d": d}

# Generate and save keys
my_keys = generate_keys(key_size)

# Save public key
public_filename = f"{file_base}_public_key.json"
with open(public_filename, "w") as f:
    json.dump({"N": my_keys["N"], "e": my_keys["e"]}, f)
print(f"[+] Public key saved to '{public_filename}'")

# Save private key
private_filename = f"{file_base}_private_key.json"
with open(private_filename, "w") as f:
    json.dump(my_keys, f)
print(f"[+] Private key saved to '{private_filename}'")
