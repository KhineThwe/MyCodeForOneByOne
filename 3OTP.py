import secrets
import string
OTP = ''
digit = string.digits
print(digit)
#0123456789
for i in range(6):
    OTP +=str(''.join(secrets.choice(digit)))

print(OTP)
