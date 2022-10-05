import re

patron = "\\(0345\\)\s[0-9]{2}[0-9]{7}|\\+549345[0-9]{7}|^345[0-9]{7}$"

s1val = "(0345) 154123456" #(válido).
s2val = "+5493454123456" #(válido).
s3val = "3454123456" #(válido).
s4noval = "+54011123456" #(no válido).
s5noval = "34564123456" #(no válido).

print(re.findall(patron, s1val))
print(re.findall(patron, s2val))
print(re.findall(patron, s3val))
print(re.findall(patron, s4noval))
print(re.findall(patron, s5noval))