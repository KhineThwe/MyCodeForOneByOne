#unpacking
#extended unpacking

#list extended unpacking
a,*b = [1,2,3,4,5,6,7]#* nae နဲ့တွဲသုံး #list tuple မှာအဆင်ပြေတယ် but dictionary
#မှာတော့ ** nae right handside mhar pl use naing
#* ka both left and right use naing
print(a)#first 1 lone ka a ကနေ ပြန်လာတယ်
print(b)#ကျန်တာအကုန် b ကနေ return ပြန်လာတယ် list အနေနဲ့ return ပြန်လာတယ်


#tuple extended unpacking
a,*b = (1,2,3,4,5,6,7)
print(a)#first 1 lone ka a ကနေ ပြန်လာတယ်
print(b)#ကျန်တာအကုန် b ကနေ return ပြန်လာတယ် list အနေနဲ့ return ပြန်လာတယ်

#string extended unpacking#** နှစ်ခုသုံးလို့မရ 
a,*b,c = 'greenhackers'
print(a)
print(b)
print(c)

#extended unpacking in righthand-side
l1 = [1,2,3,4]
l2 = [4,5,6,7]
list = [l1,l2]
list1 = [*l1,*l2]
#list in list -> nested list ပုံစံ ဖြစ်နေတာ
#ae lo pone san ma pyit chin yin extended unpacking pone san lote loe ya dal
print(list)
print(list1)


#here tuple yaw list yaw ya dal
a,*b,(c,*d,e),(z,*x,y)= [1,2,3,'khinezarthwe','ncc']
print(a)
print(b)
print(c)
print(d)
print(e)
print(z)
print(x)
print(y)
#d pone so * 2 လုံး use loe ya
#unpack lote chain mhar so list nae pl return pyan lr dal


index = [1,2,3,'khine','ncc']
print(index[0])
print(index[1:-1])
print(index[:])
#-1 ka last but last ma tine kin output ya mal
