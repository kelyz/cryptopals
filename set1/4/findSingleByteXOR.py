import sys
from word_score import word_score

fo = open("4.txt", "r")
fitness = word_score()
decrypted = ""
decrypted_strings = []
fitness_dict = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for ctext in fo:
    #ctext = fo.readline()
    #print ctext
    ctext = ctext.strip()#.decode("hex")
    for a in range(0,255):
        str_a = str(a)
        int_a = int(str_a, 16)
        hex_a = hex(int_a)[2:]
        print hex_a
        for c in ctext:
            try:
                decrypted += chr(int(c, 16) ^ int(hex_a, 16))
            except ValueError:
                pass
        print decrypted
        decrypted_strings.append(decrypted)
        decrypted = ""
    #print "-------end cipher-------"

for i in range(0, len(decrypted_strings)):
    x, y = fitness.score(decrypted_strings[i])
    if x > -94.0:
        print " " + str(x) + "  " + decrypted_strings[i]
    fitness_dict[decrypted_strings[i]] = x

highest = max(fitness_dict.values())

for k,v in fitness_dict.iteritems():
    if v == highest:
        print k
