#gmail တစ်ခုကို reset ချတော့မယ်ဆိုရင် ကျွန်တော်တို့ကို reset link လေး လှမ်းပေးတယ် ပေါ့နော် reset ချပေးပါဆိုပြီးတော့
#secure ဖြစ်တဲ့ url
#return URL-safe test string ကို return ပြန်ပေးတယ်

import secrets
print('Printing integer number using secrets module')
passwordresetLink = "https://khine.com/ncc/reset="
passwordresetLink+=secrets.token_urlsafe(4)#32 bytes အထိသုံးသင့်တယ် docs တွေအရ
print("Generating secure URL",passwordresetLink)
