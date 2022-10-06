#Random
#Secure by crytography
#Start writing a game using secure rand
# Random
# random.random()   return between floating point 0.0 and 1.0
#    Int (return)
#     /      \
#    /        \
#  randint    randrange
# //randint(0,9) (lower,upper)
# //randrange(0,10,2)(start,stop,step)2 ဆိုရင် 2 နဲ့ စားလို့ပြတ်တဲ့ number တွေ
# default of step = 1
#random.sample(population,k)  ==>population ဆိုတာ example list,set or tuple return list
#count of the total elements depend on the size of k.
#random.choice(listvalue)#list tuple dictionary တွေထဲကနေ random value တစ်ခုထုတ်ပေးတာ
#######
#random.seed() သူ့ကိုသုံးရင်secure မဖြစ်ဘူး။
#random.seed(5)
#seed method is used to PRNGs(pseudorandom number generator)
#seed value is not present (system current time)
#ဘာမှမထည့်ပေးထားရင်ကွန်ပျူတာရှိ current time ကိုယူပြီး random no ထုတ်ပေးတယ်။
######
#random.shuffle(list or set or tuple or dictionary etc)

#######
#random.uniform(start,end) in out -->floating point,return floating point number
#####
#random.triangular(low,high,mode) for floating number
#lower <=N <=Upper

import random
random_no = random.random()
print("Random No is: ",random_no)
print("Random randomint no is: ",random.randint(0,5))
print("Random random randrange no is: ",random.randrange(0,10,2))

#For random.choice
name = ['khine','zar','thwe','aung','aung']
print('Select element: ',random.choice(name))

#For random.sample
subject = ['python','java','c','c++','c#','js']
print('Select element',random.sample(subject,3))

#For random.seed(5)
random.seed(10)
print("Random no from seed(): ",random.random())

#random.shuffle
name = ['khine','zar','thwe','aung','aung']
print("Before shuffle",name)
random.shuffle(name)
print("After shuffle",name)

#random.uniform
print("Uniform",random.uniform(10.5,20.5))

#random.triangular (rand range nae tu)
print("Triangular",random.triangular(10.5,20.5,2.5))
