#in c
# int array = {1,2,3,4,5}
#int array ဆိုရင် int ပဲထည့်လို့ရတာ but python list မှာတော့ အကုန် ထည့်လို့ရတယ်။
#List methods
#List ထဲကို data ထည့်ချင်လျှင်သုံး
#1.append
#2.extend
#3.insert
my_list = [1,2,3,4]
my_list.append(6)
print(my_list)

my_list.append([6,7])
print(my_list[5])
print(my_list[5][1])

#2 ခုဆက်တိုက် list ကိုတိုးချင်ရင် extend လုပ်သင့်တယ်
numbers = [11,12,13,41,15]
my_list.extend(numbers)
print(my_list)

# ဖြတ်ထည့်ချင်ရင် insert ကို သုံးတယ် 
numbers.insert(3,"Khine")
print(numbers)

#.ခံပြီးခေါ်ရင် method ရိုးရိုးဆို function 
print(len(my_list))
