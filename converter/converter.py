## Converter of units

## Convert Kilogram and Pound
print('Conversion from liters to pounds or pounds to liters')
quantity = int(input('What amount?: '))
unit = input('Enter (K) for kilogram or (P) for pound: ')
if unit.upper() == "K":
    converted = quantity / 2.20462
    converted_round = round(converted, 2)
    print(f"The quantity in kilogram is {converted_round} kilos")
else:
    converted = quantity * 2.20462
    converted_round = round(converted, 2)
    print(f'The quantity in pound is {converted_round} pound')

################################################################################################
################################################################################################

## Convert Gallon and Liter
print('Conversion from gallon to liter or liter to gallon')
quantity = int(input('What amount?: '))
unit = input('Enter (G) for Gallon or (L) for Liter: ')
if unit.upper() == "G":
    converted = quantity / 3.785
    converted_round = round(converted, 2)
    print(f"The quantity in gallon is {converted_round} gallon")
else:
    converted = quantity * 3.785
    converted_round = round(converted, 2)
    print(f'The quantity in liter is {converted_round} liter')

################################################################################################
################################################################################################