from random import choice
import string

characters = string.ascii_letters + string.digits + string.punctuation
size = 16
password = ''

for p in range(size):
    password += choice(characters)

print(password)
