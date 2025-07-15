def IntegerToRoman(num):
    RN = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman = ''

    for key, value in RN.items():
        while num >= key:
            roman = roman + value
            num = num - key

    return roman

num = int(input('Enter any number: '))
print(IntegerToRoman(num))