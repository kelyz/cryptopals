"""
Description: Convert a hex string (passed in as command line arg) to a base 64 string
Usage: python3 hexToBase64.py [hex_string]
Output: [hex_string] in Base 64 format
"""
import sys

#print sys.argv[1].encode("base64")
#print ""
encoded = sys.argv[1].decode("hex").encode("base64", "strict")
print encoded,
