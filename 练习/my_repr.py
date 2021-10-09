class test:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    # def __repr__(self):
    #     return "Class_Test[name="+self.name+",age="+str(self.age)+"]"

    def __str__(self):
    #     return ''.format(self.name,self.age)
        return "Class_Test[name="+self.name+",age="+str(self.age)+"]"

t = test("Zhou",30)

print(t)