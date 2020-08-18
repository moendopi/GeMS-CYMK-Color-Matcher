# CMYK Color Chart Matcher Tool
# This tool takes input in the form of a CMYK form from Illustrator (or anywhere really)
# And gives the closest correponding USGS CMYK Color Chart code

from color_code_dict import color_dict

print("Please enter your CMY values.")
print("K will automatically be 0.\n")

nums = "0123456789"
user_cmyk = []
fgdc_cymk = ''
new_color = ''
fgdc_c = ''
fgdc_m = ''
fgdc_y = ''

def CMYK_to_FGDC(num):
    # 0%
    if num < 6:
        fgdc = "0"
    # 8%
    elif num <= 10 and num >= 6:
        fgdc = "A"
    # 13%
    elif num <= 16 and num >= 10:
        fgdc = "1"
    # 20%
    elif num <= 24 and num >= 16:
        fgdc = "2"
    # 30%
    elif num <= 34 and num >= 25:
        fgdc = "3"
    # 40%
    elif num <= 44 and num >= 35:
        fgdc = "4"
    # 50%
    elif num <= 54 and num >= 45:
        fgdc = "5"
    # 60%
    elif num <= 64 and num >= 55:
        fgdc = "6"
    # 70%
    elif num <= 75 and num >= 65:
        fgdc = "7"
    # 100%
    elif num > 75:
        fgdc = "X"
    return fgdc


def get_color_tile(code):
    return color_dict.get(code)

while new_color != "n": 

    try:
        c = int(input("C: "))
    except ValueError:
        print("\nEnter a number 0-100.")
        c = int(input("C: "))

    try:
        m = int(input("M: "))
    except ValueError:
        print("\nEnter a number 0-100.")
        m = int(input("M: "))

    try:
        y = int(input("Y: "))
    except ValueError:
        print("\nEnter a number 0-100.")
        y = int(input("Y: "))


    user_cmyk.append(c)
    user_cmyk.append(m)
    user_cmyk.append(y)
    user_cmyk.append(0)

    fgdc_cymk += CMYK_to_FGDC(c)
    fgdc_cymk += CMYK_to_FGDC(m)
    fgdc_cymk += CMYK_to_FGDC(y)

    tile = get_color_tile(fgdc_cymk)


    print("\nFor the CMYK values {} entered, use FGDC tile: {} (cmy value {})".format(user_cmyk, tile, fgdc_cymk))
    new_color = input("\nWould you like to enter a new color? ").lower()
    user_cmyk = []
    fgdc_cymk = ''

