from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

plaintext = "Hello"

hashed = pwd_context.hash(plaintext)

print(hashed)

print(pwd_context.verify(plaintext, hashed))