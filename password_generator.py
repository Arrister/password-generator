import random
import string

def pass_gen(length: int=10):
    alphabets = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabets) for i in range(length))
    return password

print("Strong Password Generated :", pass_gen())