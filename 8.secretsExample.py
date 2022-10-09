import secrets
import string
  
alphabet = string.ascii_letters + string.digits
print(alphabet)
password = ''.join(secrets.choice(alphabet) for i in range(10))
  
print("My Password is",password)
