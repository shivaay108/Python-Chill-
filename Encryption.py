from cryptography.fernet import Fernet

# generating key
key = Fernet.generate_key()

plainText = input("Enter the text : " ).encode()

f = Fernet(key)

encrypted_data = f.encrypt(plainText)

print("the ecrypted data is  : " , encrypted_data)

decrypted_data = f.decrypt(encrypted_data)

print("decrypted data is : "  , decrypted_data)

print("Key is : " , key)