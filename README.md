RSA Encryption & Decryption

This Python program demonstrates the RSA encryption and decryption process. It generates prime numbers p and q, computes the public and private key pairs, and performs encryption and decryption of a given message.
How It Works

    Prime Number Generation: The program generates two random prime numbers p and q greater than 20.
    Key Pair Generation: Using p and q, the program computes:
        n=p×qn=p×q
        ϕ(n)=(p−1)×(q−1)ϕ(n)=(p−1)×(q−1)
        A public key (e, n) where e is chosen such that gcd⁡(e,ϕ(n))=1gcd(e,ϕ(n))=1
        A private key (d, n) where d≡e−1mod  ϕ(n)d≡e−1modϕ(n)
    Encryption: The message is encrypted using the public key.
    Decryption: The encrypted message is decrypted using the private key.

Prerequisites

    Python 3.x
    random module
    sys module

Usage

Clone the repository: 

    git clone https://github.com/TaukTauk/RSA-key-Generation-Encryption-Decryption/

Navigate to the project directory:

    cd RSA-key-Generation-Encryption-Decryption/

Run the program:

    python3 rsa_encryption.py

    Enter your key message when prompted.

Example

    Enter your key message: Hello, RSA!
    The value of p :  719
    The value of q :  653
    Public key pair -> (e,n):  (127889, 469507)
    Private key pair -> (d,n):  (178273, 469507)
    Original message: Hello, RSA!
    Encrypted message: [312215, 277889, 249121, 249121, 191278, 65110, 106322, 312215, 213265, 120297, 191278]
    Decrypted message: Hello, RSA!

Functions

is_prime(num): Checks if a number is prime.
gcd(a, b): Computes the greatest common divisor of a and b.
mod_inverse(e, phi): Computes the modular inverse of e mod phi.
generate_keypair(bits): Generates the public and private key pairs.
encrypt(public_key, message): Encrypts the message using the public key.
decrypt(private_key, encrypted_message): Decrypts the message using the private key.
get_random_prime_greater_than_20(): Generates a random prime number greater than 20.

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
