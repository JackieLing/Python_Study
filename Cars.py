age=12

if age<14:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print("your admission cost is $"+str(price)+".")