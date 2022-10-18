#namespace
#global namespace ====> global var nae sin tal
#module သို့မဟုတ် library တွေမှာ ပါလာတဲ့ကောင်တွေကလည်း global namespace
#local namespace#block scope တစ်ခု or fun တစ်ခုအတွင်းမှာ ရှိရင် local namespace 
#built-in namespace  --> python install lote lite tr nae တစ်ပြိုင်တည်း ယူသုံးလို့ရတာကို
from math import log2,log10,log1p #global namespace
a = 20
def outerFun(a):
    print(a)
    a = 20
    b= 30#local namespace
    def innerFun(a):
        print(a)
        a = 30
# outerFun(a)
