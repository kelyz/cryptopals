import sys

str1 = sys.argv[1].decode("hex")
str2 = sys.argv[2].decode("hex")
str3 = []
str4 = ""
for c1, c2 in zip(list(str1), list(str2)):
    str3.append(chr(ord(c1) ^ ord(c2)))

for x in str3:
    str4 += x

str4 = str4.encode("hex")

print str4,
