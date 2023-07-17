sayi1=int(input("birinci sayiyi giriniz"))
sayi2=int(input("ikinci sayiyi giriniz"))

if(sayi1>sayi2):
    kucuk=sayi2
else:
    kucuk=sayi1
    
for i in range(1,kucuk):
    if(sayi1% i==0) and (sayi2%i == 0):
        ebob=i
        ekok=(sayi1*sayi2)
        
print("ebob {}".format(ebob))
print("ekok {}".format(ekok))
