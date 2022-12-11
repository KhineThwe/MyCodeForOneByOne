#seek fun ka file pointer ကိုကိုယ်လိုချင်တဲ့ position ရောက်အောင်ရွေ့ချင်တဲ့အခါအသုံးပြုတယ်
#seek fun ka python 2,3 mhar သုံးတဲ့ ပုံချင်းမတူဘူး
#seek function takes two parameters ---> offset,whence ---> 2,0--> whence ---> 0 nay yar mhar 1,2 pl htet shi naing
# 2,0 ဆိုရင် file အစကနေ 2 နေရာကိုသွားမယ်လို့ပြောခြင်းဖြစ်တယ်
#whence ----> 0 ka file start of file , 1 ka current pos , 2 ka end of file
#above python 2
#in python 3 ---> use os module
#seek_set nae seek_end shi tal
#file.seek(file.tell()-5,os.SEEK_SET) ---> လက်ရှိရောက်နေတဲ့နေရာကနေ ၅နေရာနောက်ရွေ့
#file.seek(0,os.SEEK_END)
#https://paiza.io/projects/EYZEPIE2ZqeAWiC74Lat-Q?language=python
#run above
import os
with open("data.txt","a+") as file:
    if file:
        print("Current position",file.tell())
        file.seek(2,os.SEEK_SET)#current position to 2
        print("Current moving 2 position",file.tell())
        file.seek(0,os.SEEK_END)
        print("Current position", file.tell())
        # file.seek(file.tell()-5,os.SEEK_SET)#လက်ရှိရောက်နေတဲ့ position ka nay 5 ရွေ#12-5 = 7
        # print("Current position", file.tell())
        file.seek(5, os.SEEK_SET)  # မူရင်းအစ position ka nay 5 ရွေ#12-5 = 7
        print("Current position", file.tell())
        file.seek(5, os.SEEK_SET)  # လက်ရှိရောက်နေတဲ့ position ka nay 5 ရွေ#12-5 = 7
        print("Current position", file.tell())
    else:
        print("something wrong")

#python 2 မှာ ဘာမှမရှိလဲ ရှေ့ကိုထပ်ထပ်ပြီးထောက်သွားတာ
#python 3 မှာကျ အဆုံးကနေပြီးတော့ နောက်ပဲပြန်သွားလို့ရတယ်
