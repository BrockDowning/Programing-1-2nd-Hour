EggCount = int(input("Enter Egg Amount Here : "))
dozen = EggCount / 12
Price = 0
if dozen < 4:
    Price = dozen * 0.5
elif dozen > 4 < 6:
    Price = dozen * 0.45
elif dozen > 6 < 11:
    Price = dozen * 0.40
elif dozen > 11:
    Price = dozen * 0.35
dozen = EggCount / 12 
dozenremain = dozen * 0.12
finalprice = Price * EggCount
print "Price = $" + str(finalprice)

input()
