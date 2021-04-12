import names
import random

class Bot:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

botlist=[]

def generate_bots():
    for i in range(0,9):
        if(random.randint(0, 100)%2==0):
            botlist.append(Bot(names.get_full_name(gender='male'),random.randrange(18, 60),'Male'))
        else:
            botlist.append(Bot(names.get_full_name(gender='female'),random.randrange(18, 60),'Female'))
    return botlist

botlist=generate_bots()
for i in botlist:
    print(i.name+' '+str(i.age)+' '+i.gender)

