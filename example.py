Q = int(raw_input ("digit :\n"))
d1 = 25
d2 = 10
d3 = 1
if Q >= 100:
    print('Your discount: ' + str(d1) +"%")
elif Q >= 50:
    print('Your discount: ' + str(d2) +"%")
elif Q >= 10:
    print('Your discount: ' + str(d3) +"%")
else:
    print('You need to bring more for our discount')
print("Thank's!")
range = range (50,61)
if Q in range:
    print ("{} Wins! Congradulations!").format(Q)
else:
    print ("{} Lose! Try again!").format(Q)