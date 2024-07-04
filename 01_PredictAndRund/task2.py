import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile("$This")
match = reg2.search(text)
print(match)

reg2 = re.compile("^This")
match = reg2.search(text)
print(match)

reg2 = re.compile("This^")
match = reg2.search(text)
print(match)

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart.\$") # backslash escapes and says is there a real point
match = reg2.search(text)
print(match)

reg2 = re.compile("Walmart.$") # would match if there was a w instead of a dot since its a wildcard
match = reg2.search(text)
print(match)

reg2 = re.compile("......$") # would match all last 7 characters in the string
match = reg2.search(text)
print(match)

