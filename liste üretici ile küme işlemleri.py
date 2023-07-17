
x=["python","java","php","ruby","sql"]
y=["perl","python","ruby","scala","java"]
xfarky=[i for i in x if i in x and i not in y]
xkesisimy=[i for i in x if i in x and i in y ]
xBirlesimy=xfarky+xkesisimy

print("Kümelerin farkı\n",xfarky)
print("Kümelerin kesisimi\n",xkesisimy)
print("Kümelerin Birlesimi\n",xBirlesimy)