class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('{}在吃饭'.format(self))

    def sleep(self):
        print('{}在睡觉'.format(self))

    def play(self):
        print('{}在玩'.format(self))

class Persion(Animal):
   def __init__(self,name,pets,age=1):
       super().__init__(name,age)
       self.pets = pets

   def __str__(self):
        return '我是名字叫做{}，今年{}岁人'.format(self.name,self.age)

   def yang_pets(self):
        # print(self)
        for pet in self.pets:
            pet.eat()
            pet.sleep()
            pet.play()

   def make_pet_work(self):
        for pet in self.pets:
            pet.work()

class Cat(Animal):
    def __str__(self):
        return '我是名字叫做{}，今年{}岁的小猫'.format(self.name,self.age)

    def work(self):
        print('{}在捉老鼠'.format(self))

class Dog(Animal):
    def __str__(self):
        return '我是名字叫做{}，今年{}岁的小狗'.format(self.name,self.age)

    def work(self):
        print('{}在看家'.format(self))

c = Cat('小花',2)
d = Dog('小黄',3)
p = Persion('ty',[c,d],18)
p.yang_pets()
p.make_pet_work()