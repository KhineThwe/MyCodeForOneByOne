#File Handling Mechanism
#1.File open ----> mode "r" "w" "a"
#basicအနေနဲ့ ၃မျိုးသိရင်ရပီ but total anay nae so 12 မျိူးရှိတယ်
#r --> read , w ---> write , a ----> append
#r ka file shi yin open tal but file ma shi yin problem shi tal --> IOError တက်လိမ့်မယ်
#w ka file mashi yin file 1 ku create lote pay tal
#rb so read mal binary mode nae
#r+ ---> read , write
#rb+ read and write in binary format
#2.File close ----> မဟုတ်ရင် os မှာဖွင့်လျက်တန်းလျက်ဖြစ်နေမယ်
#filepointer = open("hello.txt","r") file name and mode
#file open တာ success ဖြစ်ရင် file object တစ်ခုပြန်ပေးတယ်

file = open("data.txt","w")
if file:
    print("Success of opening file")
else:
    print("Fail of opening file")
