import re

phone = "2004-959-559  Acesta este un numar de telefon"

num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Sterge orice din sting mai putin numere
num = re.sub(r'\D', "", phone)
print "Phone Num : ", num
