import secrets
print('Printing integer number using secrets module')

print(secrets.token_bytes(2))
#ထည့်လိုက်တဲ့ byte ပေါ်မှာ မူတည်ပြီးတော့ ထည့်ပေးတယ် format ကျကျ မဟုတ်ဘဲ
#string တွေ ထွက်လာတယ်
print(secrets.token_hex(2)) 
#1 byte change to two hex digits 
#2 byte ထည့်ပေးလိုက်ရင် ၄လုံးထွက်လာတယ်။
#secrets.token_urlsafe(4)
