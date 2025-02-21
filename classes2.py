class Omkar:
    def __init__(self,name,age,branch):
        self.name=name 
        self.age=age 
        self.branch=branch 
    
    def getData(self):
        print(f"name {self.name} age {self.age} studying {self.branch} at tier 3")
Obj=Omkar("omkar",20,"cse")
Obj.getData()