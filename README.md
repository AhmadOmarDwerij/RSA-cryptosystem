
**RSA** (Rivest–Shamir–Adleman) is one of the most widely used public-key cryptographic systems. It enables secure communication over insecure channels such as the internet.

##  Key Components

- **Public Key** `(N, e)`: Used to encrypt messages. Can be shared freely.
- **Private Key** `d`: Used to decrypt messages. Must be kept secret.
- `N = p × q`, where `p` and `q` are large prime numbers.

## How RSA Works

### 1. Key Generation
1. Choose two large prime numbers `p` and `q`.
2. Compute `N = p * q`
3. Compute Euler's totient: `φ(N) = (p - 1) * (q - 1)`
4. Choose a public exponent `e` (commonly `65537`)
5. Compute the private exponent `d` such that:


d ≡ e⁻¹ mod φ(N)

### 2. Encryption
Convert the message to an integer `m`:


ciphertext = m^e mod N


### 3. Decryption


message = ciphertext^d mod N

Convert the decrypted integer back to a string.

---

## Security Note

RSA security depends on the difficulty of factoring a large number `N` into its prime factors `p` and `q`. The larger the key size (e.g., 2048 bits), the more secure the encryption.

- **128–256 bits**: Weak, for educational/demo purposes only.
- **2048 bits**: Industry standard for strong security.

---

## Example Files in This Project

- `generate_keys.py` – Generates RSA keys and saves them
- `encrypt_message.py` – Encrypts a message using a friend's public key
- `decrypt_message.py` – Decrypts a message using your private key

---

## Tips

- Keep your private key **safe and secret**.
- Only share your public key.
- Never use RSA to directly encrypt large files. Use it to encrypt symmetric keys (e.g., for AES) instead.

---


Steps:                          

| Receiver generates `(N, e, d)`                
| Receiver gives you `(N, e)`                   
| You encrypt with `(N, e)` and send ciphertext 
| Receiver decrypts with `d`                    



| Key      | Keep Secret? | Share? |
|----------|--------------|--------|
| N        | No           | Yes    |
| e        | No           | Yes    |
| d        | Yes          | No     |
| p, q     | Yes          | No     |
