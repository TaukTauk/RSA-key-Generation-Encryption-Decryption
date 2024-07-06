#the following program outputs the value of prime numbers p and q, 
#and the process of encryption and decryption along the public-private key pair
import random
array=[]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    #Calculate the greatest common divisor.
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    original_phi = phi

    while phi != 0:
        q = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2 - q * x1, x1
        y1, y2 = y2 - q * y1, y1

    if x2 < 0:
        x2 += original_phi

    return x2

def generate_keypair(bits):
    #insertion of private and public keys into the array
    p, q = array[0], array[1]

    n = p * q
    phi = (p - 1) * (q - 1)

    #Choosing a random integer e (1 < e < phi) 
    # such that e and phi are co-prime
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, message):
    #encrypting the key_msg using the secret key
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(private_key, encrypted_message):
    #decrypting the secret key using the secret key
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

#Generate a random prime number greater than 20
def get_random_prime_greater_than_20():
    while True:
        random_number = random.randint(21, 1000)
        if is_prime(random_number):
            return random_number
        
#interating function 2 times
for x in range(2):
    random_prime = get_random_prime_greater_than_20()
    array.append(random_prime)

if __name__ == "__main__":
    bits = 1024
    public_key, private_key = generate_keypair(bits)

    message = input("Enter your key message: ")
    encrypted_message = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, encrypted_message)

    print("The value of p : ", array[0])
    print("The value of q : ", array[1])
    print("Public key pair -> (e,n): ",public_key)
    print("Private key pair -> (d,n): ",private_key)
    print(f"Original message: {message}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
