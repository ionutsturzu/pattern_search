class Cautmail:
    def __init__(self,text):
        self.text = text
    def find_email(self):
        return re.search("[\w\.\-]+\@[\w]+\.[a-z]{2,3}$",self.text)

b = Cautmail("ionut@yahoo.com trebuie sa trimita un mail catre maria@gmail.com")
print(b.find_email)
