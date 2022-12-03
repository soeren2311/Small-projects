## Converter of units

## Convert Kilogram and Pound
print('Conversion from kilogram to pounds or pounds to kilogram')
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

## Convert meter and foot
print('Conversion from meter to foot or foot to meter')
length = int(input('What length?: '))
unit = input('Enter (M) for Meter or (F) for Foot: ')
if unit.upper() == "M":
    converted = length / 3.28084
    converted_round = round(converted, 2)
    print(f"The length in meter is {converted_round} meter")
else:
    converted = length * 3.28084
    converted_round = round(converted, 2)
    print(f'The length in foot is {converted_round} foot')

################################################################################################
################################################################################################

## Convert meter and yard
print('Conversion from meter to yard or yard to meter')
length = int(input('What length?: '))
unit = input('Enter (M) for Meter or (Y) for Yard: ')
if unit.upper() == "M":
    converted = length / 1.09361
    converted_round = round(converted, 2)
    print(f"The length in meter is {converted_round} meter")
else:
    converted = length * 1.09361
    converted_round = round(converted, 2)
    print(f'The length in yard is {converted_round} yard')

################################################################################################
################################################################################################

## Convert inc and Centimeter
print('Conversion from inch to centimeter or centimeter to inch')
length = int(input('What length?: '))
unit = input('Enter (I) for Inch or (C) for Centimeter: ')
if unit.upper() == "I":
    converted = length / 2.54
    converted_round = round(converted, 2)
    print(f"The length in inch is {converted_round} inch")
else:
    converted = length * 2.54
    converted_round = round(converted, 2)
    print(f'The length in centimeter is {converted_round} centimeter')
