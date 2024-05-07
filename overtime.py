#Chapter 3 Exercise 1#
Hours = input('Enter hours: ')
Rate = input ('Enter rate: ')
if int(Hours) <= 40:
    Pay = int(Hours) * float(Rate)
if int(Hours) >= 40:
    Pay = (int(Hours) * float(Rate)) + (0.5 * float(Rate) * (int(Hours)-40))
print('Pay:', Pay)
