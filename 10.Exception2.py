#try:
#   မိမိ run ချင်သော code
#except:
#   exception ဖြစ်လာခဲ့ပြီဆိုလျှင် အလုပ်လုပ်ပါ။
#finally:
#   ဘယ်လိုအခြေအနေပဲဖြစ်ဖြစ်အလုပ်လုပ်မည်။
#try code ထဲမှာရှိတဲ့ကောင်အလုပ်လုပ်ရင် else block ပါ လိုက်အ လုပ်လုပ်တယ်

try:
    file = open("data9999.txt","r")
    # data = int(input("Please enter valid key"))
except Exception as err:
    print(err)
finally:
    print("This else statement is running")
