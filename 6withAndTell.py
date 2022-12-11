#with statement ka file handling mhar so useful
#exception တွေဖြစ်လာရင် file ကို auto off ပေးတယ်
#x mode ka just file open ma shi yin create
# fileptr = open("testx.txt","x")
# print(fileptr)
with open("data.txt","r") as file:
    if file:
        print("The file pointer at byte: ",file.tell())
        contents = file.read()
        print("pointer is at byte: ",file.tell())
    else:
        print("something wrong")

#w mode mhar file data တွေက overwrite ဖြစ်သွားတယ် ဘာလို့လဲဆိုရင် file pointer ka ထိပ်ဆုံးကောင်ကို pointer ထောက်ထားလို့
#a mode ka data ရဲ့နောက်ဆုံးကောင်ကိုထောက်ထားတာ
#tell method ---> file pointer return pyan pay tal
#r ---> 0
#w ----> 0
#a ---> last
#char 1 lone ko 1byte --> char's Ascii value က 1 byte ထက်မပိုဘူး default encoding mhar
#encoding paw မူတည်ပြီးပြောင်းနိုင်
