# #map function
# def fact(n):
#     return 1 if n < 2 else n*fact(n-1)
# #recursive fun mhar terminating point pr ya mal otherwise overflow
# #iterable ka list,tuple doe
#
# #function yal iterable
# result = map(fact,range(6))
# print(result)#map object return
#
# for i in result:
#     print(i)
#
# for x in result:
#     print(x)
# #တကယ်ဆိုရင်နှစ်ခါ ဖြစ်သင့်ပေမဲ့ map ka တစ်ကြိမ်မှာတစ်ခုပဲပြန်ပေး


#free error
#map function
def fact(n):
    return 1 if n < 2 else n*fact(n-1)
#recursive fun mhar terminating point pr ya mal otherwise overflow
#iterable ka list,tuple doe

#function yal iterable
result = list(map(fact,range(6)))#here fix it ---> dlo lote pay yin generator pyan pay tr
print(result)#map object return

for i in result:
    print(i)

for x in result:
    print(x)
#တကယ်ဆိုရင်နှစ်ခါ ဖြစ်သင့်ပေမဲ့ map ka တစ်ကြိမ်မှာတစ်ခုပဲပြန်ပေး map function ka generator fun ko pl return pyan pay
#generator fun ka call tine 1 ku 1 ku pyan pay tal lone wa asone ma that thwar buu

