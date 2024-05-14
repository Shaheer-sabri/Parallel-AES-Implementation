from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from queue import Queue
import threading
import time

def encrypt_chunk(data_chunk, key, queue, lock):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_data = pad(data_chunk, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    with lock:
        queue.put((cipher.iv, encrypted_data))

def decrypt_chunk(encrypted_chunk, iv, key, queue, lock):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_chunk)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    with lock:
        queue.put(unpadded_data)

def parallel_encrypt(data, key, num_threads):
    start_time = time.perf_counter()
    chunk_size = (len(data) // num_threads) + (AES.block_size - (len(data) % num_threads) % AES.block_size)
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    result_queue = Queue()
    lock = threading.Lock()
    threads = []
    for chunk in data_chunks:
        thread = threading.Thread(target=encrypt_chunk, args=(chunk, key, result_queue, lock))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    encrypted_data = []
    while not result_queue.empty():
        encrypted_data.append(result_queue.get())
    end_time = time.perf_counter()
    print(f"Encryption Time: {end_time - start_time:.6f} seconds")
    return encrypted_data

def parallel_decrypt(encrypted_data, key, num_threads):
    start_time = time.perf_counter()
    result_queue = Queue()
    lock = threading.Lock()
    threads = []
    for iv, chunk in encrypted_data:
        thread = threading.Thread(target=decrypt_chunk, args=(chunk, iv, key, result_queue, lock))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    decrypted_data = []
    while not result_queue.empty():
        decrypted_data.append(result_queue.get())
    end_time = time.perf_counter()
    print(f"Decryption Time: {end_time - start_time:.6f} seconds")
    return b''.join(decrypted_data)

def main():
    key = get_random_bytes(16)
    data = b"Hello, welcome to AES encryption! " * 100000000  # Adjusted for practical testing
    num_threads = 6
    print("Original Data Length:", len(data))

    encrypted_data = parallel_encrypt(data, key, num_threads)
    decrypted_data = parallel_decrypt(encrypted_data, key, num_threads)

    print("Decryption Verification:", data == decrypted_data)
    if data != decrypted_data:
        print("Mismatch between original and decrypted data.")

if __name__ == "__main__":
    main()
