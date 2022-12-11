#exceptional handling --> try except finally
#detect =====> error ---> file ma shi yin os error ---> os nae ဆိုင်တဲ့ error ka 50 လောက်ရှိတယ်
#not permitted ---> error no 1
# a = 10
# b = 0
# c = 10/0#Zero division error
# a  = 10 * data *3#name error
# b = 10+'data'#type error
#try:
#   မိမိ run ချင်သော code
#except:
#   exception ဖြစ်လာခဲ့ပြီဆိုလျှင် အလုပ်လုပ်ပါ။
#else:
#   exception မဖြစ်လာခဲ့ရင် လုပ်တယ်။
#try code ထဲမှာရှိတဲ့ကောင်အလုပ်လုပ်ရင် else block ပါ လိုက်အ လုပ်လုပ်တယ်

try:
    file = open("data9.txt","r")
    # data = int(input("Please enter valid key"))
except:
    print("File cannot open")
else:
    print("This else statement is running")
