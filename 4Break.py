#break
#continue
#different between break and continue

for va in "khine":#va ဆိုတာ variable တစ်လုံးသက်သက်ပဲ ပထမအကြိမ် loop ပတ်တဲ့အချိန်မှာ va က k second =>h
    if va == 'i':#first time မှာ va ကို ကျွန်တော်တို့က k လို့မြင်ကြည့်ရမှာ 
        break#break လုပ်တယ်ဆိုတာသူနဲ့သက်ဆိုင်တဲ့ code block ကြီးတစ်ခုလုံးကို အကြိမ်ကြိမ်အခါအခါ အလုပ်လုပ်နေတဲ့ iterator
    #for loop ကြီးတစ်ခုလုံးကို break လုပ်ပစ်လိုက်တာ
    print(va)
print('___________ending')

for var in "khine":
    if var == 'i':
        continue#continue ဆိုတာ သူ့ကိုမြင်တာနဲ့ code block ကနေထွက်မသွားဘဲ code block အစကို ပြန်သွားမယ်
    print(va)
print('___________ending')
