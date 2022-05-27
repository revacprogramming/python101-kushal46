# Strings

 text = "X-DSPAM-Confidence:    0.8475"
 i = text.find('0.8475')
 s = slice(i,50)
 ans = float(text[s])
 print(ans)
