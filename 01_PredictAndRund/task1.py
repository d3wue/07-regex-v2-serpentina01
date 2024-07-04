import re # import the re package

text = "This book on tennis cost $3.99 at Walmart. tennis" # test is defined

reg1 = re.compile("ten") # make a regular expression with ten
match = reg1.match(text) # ten isn't at the beginning of text
print(match)

reg2 = re.compile("this") # defines a regular expression
match = reg2.match(text) # this is not at the beginning of text since this is in lower case
print(match)

reg3 = re.compile("This")
match = reg3.match(text) # will find This in text at the beginning
print(match)
print(match.group(0)) # ?

match = reg1.search(text) # gives me only the first location 
print(match)
print(text[13:16])

match = reg1.findall(text) 
print(match)