# Strings
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
#print(pos)
val=text[pos+5:]
#print(val)
print(float(val))
#dec=float(val)
#print(dec)