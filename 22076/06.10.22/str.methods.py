##    STRING METHODS

''' 1.capitalize()
Converts the first character to upper case '''

##s="happy new year"
##print(s.capitalize())

''' 2.casefold()   and lower()
Converts string into lower case '''

##s="PYTHON"
##print(s.casefold())
##print(s.lower())

''' 3.center()
Returns a centered string '''

##s="python"
##print(s.center(50))

''' 4.count()
Returns the number of times a specified value occurs in a string '''

##s="happy new year"
##print(s.count("y"))

''' 5.encode()
Returns an encoded version of the string '''

s="python"
##x=s.encode()
##print(x)

'''6.endswith()
Returns true if the string ends with the specified value '''

##s="python"
##print(s.endswith("n"))

'''7.expandtabs()
Sets the tab size of the string '''

##s="p y thon"
##x=s.expandtabs(2)
##print(x)

'''8.find()
Searches the string for a specified value and returns the position of where it was found '''

##s="python"
##x=s.find("h")
##print(x)

'''9.format()
Formats specified values in a string '''

##s="python"
##print("{} is a simple programing language".format(s))

'''10.format_map()
Formats specified values in a string '''

s={"a":7,"b":8}
print('{a} {b}'.format_map(s))

'''10.index()
Searches the string for a specified value and returns the position of where it was found '''

##s="python"
##print(s.index("t"))

'''11.isalnum()
Returns True if all characters in the string are alphanumeric '''

##s="python12"
##print(s.isalnum())

'''12.isalpha()
Returns True if all characters in the string are in the alphabet '''

##s="pYthon12"
##print(s.isalpha())

'''13.isdecimal()
Returns True if all characters in the string are decimals '''

##s="12344"
##print(s.isdecimal())

'''14.isdigit()
Returns True if all characters in the string are digits '''

##s="12344"
##print(s.isdigit())



'''15.isidentifier()
Returns True if the string is an identifier '''

##s="python_12"
##p="1python"
##print(s.isidentifier())
##print(p.isidentifier())

'''16.islower()
Returns True if all characters in the string are lower case '''

##s="python"
##l="Python"
##print(s.islower())
##print(l.islower())

'''17.isnumeric()
Returns True if all characters in the string are numeric '''

##s="p1234"
##l="12345"
##print(s.isnumeric())
##print(l.isnumeric())

'''18.isprintable()
Returns True if all characters in the string are printable '''

##s="python & !#"
##print(s.isprintable())

'''19.isspace()
Returns True if all characters in the string are whitespaces '''

##s="python"
##p=" " 
##print(s.isspace())
##print(p.isspace())

'''20.istitle()
Returns True if the string follows the rules of a title,each word start with capital letter'''

##s="Happy New Year"
##print(s.istitle())

'''21.isupper()
Returns True if all characters in the string are upper case '''

##s="PYTHON"
##print(s.isupper())

'''22.join()
Joins the elements of an iterable to the end of the string '''

##s=("happy","new","year")
##print("-".join(s))

'''23.ljust()
Returns a left justified version of the string '''

##s="python"
##print(s.ljust(10,"@"))

'''24.lower()
Converts a string into lower case '''

##s="PYTHON"
##p=s.lower()
##print(p)

'''25.lstrip()
Returns a left trim version of the string '''

##s="  python  "
##print(s.lstrip())

'''26.rstrip()
Returns a right trim version of the string '''

##s="  python  "
##print(s.rstrip())

'''27.rstrip()
Returns both left and right trim version of the string '''

##s="  python  "
##print(s.strip())


'''28.split()
Splits the string at the specified separator, and returns a list '''

##s="happy new year"
##l=s.split()
##print(l)

'''29.splitlines()
Splits the string at line breaks and returns a list '''

##s="happy\nnew\nyear"
##print(s.splitlines())

'''30.startswith()
Returns true if the string starts with the specified value '''

##p="python"
##print(p.startswith("p"))

'''31.swapcase()
Swaps cases, lower case becomes upper case and vice versa '''

##s="happy new year"
##print(s.swapcase())

'''32.title()	Converts the first character of each word to upper case '''

##s="happy new year"
##print(s.title())

'''33.translate()
Returns a translated string '''

##d ={83:  80}
##txt = "Hello Sam!"
##print(txt.translate(d))

'''34.upper()
Converts a string into upper case '''

##p="python"
##print(p.upper())

'''35.zfill()
Fills the string with a specified number of 0 values at the beginning '''

##s="11"
##print(s.zfill(10))




'''
print(x.format_map("4"))
print("casefold",x.casefold(y))
print(x.center(20,'@'))
print(x.count('p'))
print(x.encode())
print(x.endswith('n'))
print(x.expandtabs())
print(x.find("t"))
print("{}".format(x))
print("{}".format_map(y))
print("index",x.index(y))
print("isalnum",x.isalnum())
print("isalpha",x.isalpha())
print("isascii",x.isascii())
print("isdecimal",x.isdecimal())
print("isdigit",x.isdigit())
print("isidentifier",x.isidentifier())
print("islower",x.islower())
print("isnumeric",x.isnumeric())
print("isprintable",x.isprintable())
print(x.isspace())
print(x.istitle())
print(x.isupper())
print('-'.join(x))
print(x.ljust(20,"@"))
print(x.lower())
print(x.lstripe())
print(x.partition())
print(x.removeprefix("p"))
print(x.removesuffix("n"))
print(x.replace(p,k))
print(x.rfind())
print(x.rindex())
print(x.rjust())
print(x.rpartition())
print(x.rsplit())
print(x.rstrip())
print(x.split())
print(x.splitlines())
print(x.startswith())
print(x.strip())
print(x.swapcase())
print(x.title())
print(x.translate(dict))
print(x.upper())
print(x.zfill(20)) '''










