weight = float(input("Weight in lbs : "))
a = input("(K)g or (L)bs: ")
b = a.upper()
if(b=='L'):
    print("Weight in Lbs: ",weight)
elif(b=='K'):
    print("Weight in Kg: ",weight/2.2)
else:
    print()
