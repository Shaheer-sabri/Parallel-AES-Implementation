from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

def encrypt_data(data, key):
    # Ensure the data is padded to the block size of 16 bytes
    padded_data = pad(data, AES.block_size)
    # Create a new AES cipher object with the key and CBC mode
    cipher = AES.new(key, AES.MODE_CBC)
    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    # Return the IV and the encrypted data
    return cipher.iv, encrypted_data

def decrypt_data(encrypted_data, key, iv):
    # Create a new AES cipher object with the key, CBC mode and the IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)
    # Unpad the decrypted data and return
    return unpad(decrypted_data, AES.block_size)

def main():
    # Generate a random key of 16 bytes (128 bits)
    key = get_random_bytes(16)
    # Example data to encrypt
    data = b"Hello, welcome to AES encryption! " * 100000000  # Adjust for testing if necessary

    print("Original Data Length:", len(data))

    # Encrypt data
    start_time_encryption = time.perf_counter()
    iv, encrypted = encrypt_data(data, key)
    end_time_encryption = time.perf_counter()
    print("Encrypted Data Length:", len(encrypted))
    print("Encryption Time:", end_time_encryption - start_time_encryption, "seconds")

    # Decrypt data
    start_time_decryption = time.perf_counter()
    decrypted = decrypt_data(encrypted, key, iv)
    end_time_decryption = time.perf_counter()
    print("Decrypted Data Length:", len(decrypted))
    print("Decryption Time:", end_time_decryption - start_time_decryption, "seconds")

    # Verify the decryption
    assert decrypted == data, "Decryption failed, data does not match!"

if __name__ == "__main__":
    main()
