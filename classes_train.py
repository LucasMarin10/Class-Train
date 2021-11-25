#A Len test
n="Lucas"
print(len(n))
fn="Lucas T. Marin"
print(len(fn))
#Str Builder
class StrBuild():
    """Definy the String"""
    def __init__(self,string):
        self.string=string
    """Append to String"""
    def append(self,sta):
        self.sta=sta
        self.string=self.string+" "+self.sta
    def len(self):
        """Get the string length"""
        return len(self.string)
    def getStr(self):
        """Get the string"""
        return self.string
    def getTit(self):
        """Get the string with first capital leters"""
        return self.string.title()
#1 instance
mn=StrBuild("lucas")
print(mn.getStr())
print(mn.getTit())
#2 instance
mcn=StrBuild("Nova")
mcn.append("Odessa")
print(mcn.getStr())
#geting the instances length
print(mn.len())
print(mcn.len())


