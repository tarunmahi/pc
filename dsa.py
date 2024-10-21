import random
from hashlib import sha1

# Helper function to check if a number is prime
# Function to calculate the modular inverse using the Extended Euclidean Algorithm
def mod_inverse(e, phi):
    t, new_t = 0, 1
    r, new_r = phi, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("e is not invertible")
    if t < 0:
        t += phi
    return t

# RSA Key Generation
def generate_rsa_keys(bits=128):
    p = generate_large_prime(bits // 2)  # 64-bit primes
    q = generate_large_prime(bits // 2)  # 64-bit primes
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e (public exponent) such that 1 < e < phi and gcd(e, phi) == 1
    e = 65537  # It's common to use this fixed value for e
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Public key (e, n), Private key (d, n)

# RSA Sign Function
def rsa_sign(message, private_key):
    d, n = private_key
    # Hash the message using SHA-1 and truncate to 64 bits
    hashed_message = int.from_bytes(sha1(message.encode()).digest(), byteorder='big') & ((1 << 8) - 1)
    
    # Sign the truncated hash with the private key
    signature = pow(hashed_message, d, n)
    return signature

# RSA Verify Function
def rsa_verify(message, signature, public_key):
    e, n = public_key
    # Hash the message using SHA-1 and truncate to 64 bits
    hashed_message = int.from_bytes(sha1(message.encode()).digest(), byteorder='big') & ((1 << 8) - 1)

    # Verify the signature by decrypting it with the public key
    decrypted_hash = pow(signature, e, n)
    print(hashed_message)
    print("   ")
    print(decrypted_hash)
    return decrypted_hash == hashed_message
    

# Example usage
if __name__ == "__main__":
    # Generate RSA keys using 128-bit primes (64-bit for each prime)
    public_key, private_key = generate_rsa_keys(bits=16)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # The message to sign
    message = "Thi valuestimes"

    # Sign the message
    signature = rsa_sign(message, private_key)
    print("Signature:", signature)

    # Verify the signature
    is_valid = rsa_verify(message, signature, public_key)
    print("Signature valid:", is_valid)