import re
class CautIp:
    def __init__(self,text):
        self.text = text
    def find_ip_adress(self,paterntext):
        return re.findall(paterntext,self.text)



a = CautIp("Acesta 192.100.10.1 este o adresa de ip si 10.2.3.2 este tot o adresa de ip")
print(a.find_ip_adress(re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.')))
