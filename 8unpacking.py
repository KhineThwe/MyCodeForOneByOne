#List namespaces
#globla namespaces ka global var nae same pl phyit 
#module or library global namespaces
#built-in library = python ko install lote lite tr nae pr lr tae kaung tway



#unpacking
#equation yae right handside ko assign to the left handside
#list tuple pl unpacking lote loe ya dal
#set  dictionary ka unorder phyit loe unpacking lote loe ma ya

a,b,c = (10,100,1000)#tuple unpacking
print(a,b,c)


#2.data from list assign to the tuple
#we can unpack list tuple data structure achin chin 
(k,z,t)=[100,200,204]
print(k,z,t)


#string unpacking
(jh,k,l) = 'XYZ'
print(jh,k,l)

#Why we need unpacking?
#data tway ko loop pat loe ya dal
#set---->unorder
#that's why we have to do unpacking
dset1 = {'A','B','C','D'}
print(dset1)
