import re

reg = re.compile("www.google.de|com") 
print(reg.match("www.google.com")) # steht im string entweder "www.google.de" oder "com" ; dot is any wildcard; with search it would have worked

reg = re.compile("www\.google\.(de|com)") # want to find a real dot and take com and de in brackets
print(reg.match("www.google?de"))
print(reg.match("www.google.de"))
print(reg.match("wwwwgoogle.de"))

string = "Niko Stein"

reg = re.compile("Nikolai Stein")
print(reg.match(string))

reg = re.compile("Niko Stein")
print(reg.match(string))

reg = re.compile("Niko|Nikolai Stein") # finds Niko at the first four strings (0, 4)
print(reg.match(string))

reg = re.compile("(Niko | Nikolai) Stein") # too many backspaces so it is none
print(reg.match(string))

reg = re.compile("(Niko|Nikolai) Stein") # here the backspaces are correct
print(reg.match(string))

string = "\."

reg = re.compile(".") # wildcard
print(reg.match(string)) # first character I find is backslash
print(reg.findall(string)) # gives a list with bakcslash and dot

reg = re.compile("\.") 
print(reg.match(string)) # doesnt find the dot
print(reg.search(string)) # finds the dot

reg = re.compile("\\\\")
print(reg.match(string))

reg = re.compile("\\\\.")
print(reg.match(string))

reg = re.compile("\\\\\.")
print(reg.match(string))

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("is")
match = re.findall(reg, text) # finds "is" in This and tennis
print(match)

reg = re.compile("\d") # finds all figures/ wild card for figures
match = re.findall(reg, text)
print(match)



text = "This book on tennis cost $3.99 at Walmart."
reg = re.compile("3\.99") # 
match = re.search(reg, text)
print(match)

reg = re.compile("\$\d\.\d\d") # generalize the price but doesn't go for two digits
match = re.search(reg, text)
print(match)

reg = re.compile("\$\d+\.\d{2}") 
match = re.search(reg, text)
print(match)