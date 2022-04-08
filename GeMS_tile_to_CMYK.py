# GeMS to CMYK Color Matcher v. 0.01
# Author: Ben Weinmann, Oct. 2, 2020, br.weinmann@gmail.com

# This tool takes a GeMS CMYK color tile number and returns the CYMK 
# value so it can be matched in another program such as QGIS, Illustrator, Inkscape, etc.

from color_code_dict import color_dict

# this line magically swaps the key and value in the dictionary
# why is this useful? because in this case I am giving the tile code and I want the values associted with that tile 
# without have to make an entirely new dictionary which is just those values swapped!
flipped_color_dict = {value: key for key, value in color_dict.items()}

gems_cmyk_color_values = {"0":0, "A":8, "1":13, "2":20, "3":30, "4":40, "5":50, "6":60, "7":70, "X":100}
return_cmyk_value = []

tile_code = input("Enter CMYK tile code or Symbol code: ")

def get_color_tile(code):
    return flipped_color_dict.get(code)


def convert_code(tile_code):
    cmyk_tile = get_color_tile(tile_code)
    return cmyk_tile

def cmyk_to_rgb(cmyk_string):
    """Convert a cmyk color string to an rgb color string"""
    c,m,y,k = [int(val)/100 for val in cmyk_string.split(',')]
    r = str(int(255 * (1-c) * (1-k)))
    g = str(int(255 * (1-m) * (1-k)))
    b = str(int(255 * (1-y) * (1-k)))
    return ",".join((r,g,b))


cmyk_value_code = convert_code(tile_code)

for item in cmyk_value_code:
    if item in gems_cmyk_color_values:
        return_cmyk_value.append(gems_cmyk_color_values.get(item))
return_cmyk_value.append(0)

cmyk_string = ''.join(str(return_cmyk_value)).strip("[ ]")
#for item in return_cmyk_value:
#    cmyk_string += str(item) + ","

print(cmyk_string)
rgb = cmyk_to_rgb(cmyk_string)
print(rgb)

#print("CMYK = ({})".format(str(return_cmyk_value).strip('[]')))