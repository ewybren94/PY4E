Hours = input('Enter hours: ')
Rate = input ('Enter rate: ')
try:
    Hours = int(Hours)
    Rate = float(Rate)
    if int(Hours) <= 40:
        Pay = int(Hours) * float(Rate)
    if int(Hours) >= 40:
        Pay = (int(Hours) * float(Rate)) + (0.5 * float(Rate) * (int(Hours)-40))
    print('Pay:', Pay)
except:
    print('Error. Please enter a numerical value.')
