import re

# modify regular expression so you can find all of the expressions
reg = re.compile("(https?://)?www\.[a-z\-\.]+\.(com|de)[a-z/]*")

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.google.com")
print(m)

m = reg.match("http://www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.uni-wuerzburg.de/wiba/startseite/")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)