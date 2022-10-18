#unpacking ဆိုသည်မှာ equation ရဲ့ညာဘက်မှာရှိတဲ့ကောင်တွေကို equation
#ရဲ့ဘယ်ဘက်မှာရှိတဲ့နေရာဆီမှာ assign ပြန်လုပ်ပေးခြင်းဖြစ်တယ်

#iterator extended unpacking
#list တွေ tuple တွေကို လည်း unpack lote loe ya dal
#but set,dictionary တွေက unorder ဖြစ်တဲ့အတွက်ကြောင့် unpacking lote loe ma ya
a,b,c = (10,100,20)#tuple တွေကို unpack lote tr
print(a,b,c)

#list ထဲက data ကို tuple ထဲမှာ assign ပြုလုပ်လိုက်တာ
#list tuple set ae lo data structure အချင်းချင်းလည်း unpack လုပ်လို့ရတယ်
(k,z,t) = [100,200,300]
print(k,z,t)

#string unpacking
(h,j,k) = 'XYZ'
print(h,j,k)


#loop#dr ka unpacking ma hote loop ပတ်ပြီး data ထုတ်တာပဲ
dset = {1,2,3,4,5}
dset1 = {'A','B','C','D','E'}
print(dset1)#char တွေထည့်လိုက်တော့ အစဉ်လိုက်ထွက်မလာတော့ဘူး # အခုလိုတွေဖြစ်တတ်တာမို့လို့ အစဉ်လိုက်ထွက်လာ
#အောင် Unpack ပြုလုပ်ရမယ်
for d in dset1:
    print(d)
