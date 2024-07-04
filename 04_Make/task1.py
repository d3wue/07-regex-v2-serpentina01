import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here