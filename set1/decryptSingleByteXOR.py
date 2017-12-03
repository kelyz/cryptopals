import sys
#test 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"
decrypted = ""
cipher = sys.argv[1].decode("hex")

letterFrequency = {}
letterFrequency['A'] = .082;
letterFrequency['B'] = .015;
letterFrequency['C'] = .028;
letterFrequency['D'] = .043;
letterFrequency['E'] = .127;
letterFrequency['F'] = .022;
letterFrequency['G'] = .020;
letterFrequency['H'] = .061;
letterFrequency['I'] = .070;
letterFrequency['J'] = .002;
letterFrequency['K'] = .008;
letterFrequency['L'] = .040;
letterFrequency['M'] = .024;
letterFrequency['N'] = .067;
letterFrequency['O'] = .075;
letterFrequency['P'] = .019;
letterFrequency['Q'] = .001;
letterFrequency['R'] = .060;
letterFrequency['S'] = .063;
letterFrequency['T'] = .091;
letterFrequency['U'] = .028;
letterFrequency['V'] = .010;
letterFrequency['W'] = .023;
letterFrequency['X'] = .001;
letterFrequency['Y'] = .020;
letterFrequency['Z'] = .001;
letterFrequency[' '] = .200;
length = len(decrypted)
decrypted_strings = []


for c1 in alphabet:
    for c2 in cipher:
        decrypted += chr((ord(c1) ^ ord(c2)))
    #print decrypted
    decrypted_strings.append(decrypted)
    decrypted = ""
    #print "---------------------"

score = 0
decrypted_texts = {}

for i in range(0, len(decrypted_strings)):
    for c in decrypted_strings[i]:
        try:
            score += letterFrequency[c.upper()]
        except KeyError:
            pass
    print decrypted_strings[i] + " " + str(score)
    decrypted_texts[decrypted_strings[i]] = score
    score = 0

print "++++++++++++++++++++++++++++++++++"
z = max(decrypted_texts.values())
for k, v in decrypted_texts.iteritems():
    if v == z:
        print k
