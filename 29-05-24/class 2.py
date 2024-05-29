class Student:
    def __init__(self,roll,name,p,address):
        self.roll=roll
        self.name=name
        self.p=p
        self.address=address
    def disInfo(self):
        print("name:",self.name,"phone:",self.p,"address:",self.address)
std1=Student(2051,'srinidhi',7842325539,'knp')
std1.disInfo()
std2=Student(2051,'srinidhi',7842325539,'knp')
std2.disInfo()