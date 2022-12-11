#with statement ka file handling mhar so useful
#exception တွေဖြစ်လာရင် file ကို auto off ပေးတယ်
#x mode ka just file open ma shi yin create
# fileptr = open("testx.txt","x")
# print(fileptr)
with open("data.txt","r") as file:
    if file:
        contents = file.read()
        print(contents)
    else:
        print("something wrong")

#w mode mhar file data တွေက overwrite ဖြစ်သွားတယ် ဘာလို့လဲဆိုရင် file pointer ka ထိပ်ဆုံးကောင်ကို pointer ထောက်ထားလို့
#a mode ka data ရဲ့နောက်ဆုံးကောင်ကိုထောက်ထားတာ
#tell method 
