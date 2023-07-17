import random

sayilar=[random.randint(1,101) for i in range(100)]
tekSayilar=[]
ciftSayilar=[]
print("{}\n".format(sayilar))
for i in sayilar:
    if(i % 2 == 0):
        ciftSayilar.append(i)
    else:
        tekSayilar.append(i)
print("cift={}".format(ciftSayilar))
print("tek ={}".format(tekSayilar))