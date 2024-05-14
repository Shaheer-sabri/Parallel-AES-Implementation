# Parallel AES Encryption and Decryption

This project explores the parallelization of the Advanced Encryption Standard (AES) encryption and decryption processes using Python. By leveraging multithreading, we aim to improve the performance of AES operations, demonstrating the potential for parallel processing to significantly speed up data encryption and decryption.

## Authors

- Syed Shaheer Sabri (24522)
- Muhammad Danish Raza (24796)

## Institute

Institute of Business Administration

## Course

PDC - 96002

## Contents

1. [Introduction](#introduction)
2. [Methodology](#methodology)
3. [Implementation Approaches](#implementation-approaches)
4. [Results](#results)
5. [Conclusion](#conclusion)
6. [Future Work](#future-work)
7. [References](#references)

## Introduction

Data security is crucial in today's digital age, with increasing amounts of data being transmitted and stored. The AES encryption standard is widely used for securing data, but its performance can be limited by sequential processing. This project addresses these limitations by implementing parallel AES encryption and decryption using Python's multithreading capabilities.

Our goal is to demonstrate that parallel processing can enhance the speed and efficiency of AES operations without compromising security. This approach is particularly relevant for applications requiring high throughput and quick data processing.

## Methodology

The project divides the input data into smaller chunks, processes these chunks in parallel using threads, and then combines the results. Here are the key steps:

- **Data Chunking:** Divide the input data into chunks suitable for AES encryption.
- **Parallel Encryption:** Encrypt each data chunk independently in a separate thread.
- **Parallel Decryption:** Decrypt each encrypted chunk in parallel.

### Key Functions

- `encrypt_chunk(data_chunk, key, queue, lock, index)`: Encrypts a single chunk of data using AES in CBC mode.
- `decrypt_chunk(encrypted_chunk, iv, key, queue, lock, index)`: Decrypts a single chunk of encrypted data.
- `parallel_encrypt(data, key, num_threads)`: Manages the encryption process.
- `parallel_decrypt(encrypted_data, key, num_threads)`: Manages the decryption process.

### Algorithms and Techniques

- **AES in CBC Mode:** Ensures secure encryption by using an initialization vector (IV) for each operation.
- **Padding and Unpadding:** Aligns data chunks with the AES block size.
- **Multithreading:** Utilizes Python's threading module to create and manage multiple threads.
- **Thread-safe Queues and Locks:** Synchronizes threads to prevent race conditions.

## Implementation Approaches

### Task-level Parallelism

- **Task-level Parallelism:** Breaks down the AES algorithm into coarse-grained sub-tasks.
- **Instruction-level Parallelism:** Focuses on identifying sub-instructions that can be executed in parallel.
- **Special Hardware:** Uses GPUs and FPGAs for optimized parallel computation.

### Parallel AES Strategies in Python

- **Multiprocessing:** Utilizes multiple processes for true parallelism, ideal for CPU-intensive tasks.
- **Threading:** Uses lightweight threads within a single process, suitable for I/O-bound tasks.

## Results

The project successfully demonstrates the effectiveness of parallel AES encryption and decryption. The parallel approach shows significant speed improvements compared to sequential processing, especially for large data sets.

### Performance Comparison

- **Encryption:** Parallel processing provides faster encryption times as data length increases.
- **Decryption:** Similar performance gains are observed in the decryption process.

## Conclusion

The project demonstrates that parallel processing can significantly enhance the performance of AES encryption and decryption. By dividing data into chunks and processing them simultaneously, we achieve faster processing times while maintaining data security.

## Future Work

Future research could optimize chunk size and thread count for even better performance. The project could also be expanded to support other encryption algorithms and modes, and to include more sophisticated error handling and logging mechanisms. Integrating this approach into real-world applications would be a valuable next step.

## References

1. [Advanced Encryption Standard](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
2. [Geeks For Geeks: Advanced Encryption Standard (AES)](https://www.geeksforgeeks.org/advanced-encryption-standard-aes/)
3. [Devglan: AES Encryption and Decryption Online](https://www.devglan.com/online-tools/aes-encryption-decryption)
4. Aj Elbirt W. Y. (2000). An FPGA Implementation and Performance Evaluation of the AES Block Cipher Candidate Algorithm Finalists.
5. Alfred J. Menezes P. C. (1996). Handbook of Applied Cryptography. CRC Press.
6. Ferguson N. (2010). Cryptography Engineering: Design Principles and Practical Applications. Wiley.
7. Ghada F. Elkabbany H. K. (2015). A Design of a Fast Parallel-Pipelined Implementation of AES: Advanced Encryption Standard.
8. Jingang Shi S. W. (2020). A Parallel AES Encryption Algorithms and Its Application. Retrieved from [ResearchGate](https://www.researchgate.net/publication/338542389_A_Parallel_AES_Encryption_Algorithms_and_Its_Application)
9. Joan Daemen V. R. (2002). The Design of Rijndael. Springer Berlin Heidelberg.
10. Stallings W. (2017). Cryptography and Network Security: Principles and Practice 8th edition. Pearson.
11. Viega J. (2003). Secure Programming Cookbook for C and C++: Recipes for Cryptography Authentication Input Validation & More. O'Reilly Media.
12. Yongquan Yang D. W. (2021 June). Accelerating DES and AES Algorithms for a Heterogeneous Many-core Processor. Retrieved from [ResearchGate](https://www.researchgate.net/publication/350937834_Accelerating_DES_and_AES_Algorithms_for_a_Heterogeneous_Many-core_Processor)

## How to Run

### Prerequisites

- Python 3.x
- Required Python libraries: `pycryptodome`

### Usage

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required libraries:
   ```bash
   pip install pycryptodome
   ```

3. Run the encryption and decryption scripts:
   ```bash
   python parallelencryp.py
   python synchronous.py
   ```

Feel free to contribute to the project by opening issues or submitting pull requests.
