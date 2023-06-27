from random import randint

dict = {'snake':1,'water':2,'Gun':3}



class Player:
    def __init__(self,name):
        self.name = name

    def select(self):
        sel = int(input('Pick 1.Snake 2.Water 3.Gun'))



class Computer:
    def pick(self):
        select = randint(1,3)



user = Player('ayush')
comp = Computer
counter = 0
def check(user, comp):
    sel = Player.select()
    selcm = Computer.pick()

    if sel == selcm:
        return 0
    elif sel == 1 and selcm == 2:
        return {'PLayer won the game'}
    elif sel ==1 and selcm == 3:
        return {'Computer won the game'}
    elif sel == 2 and selcm == 1:
        return {'PLayer won the game'}
    elif sel == 2 and selcm == 3:
        return {'PLayer won the game'}
    elif sel == 3 and selcm ==1:
        return {'Computer won the game'}
    elif sel == 3 and selcm == 2:
        return {'Computer won the game'}
    else:
        return {'Wrong input'}



gameon = True
print("Hello lets begin the game of snake water and gun")
while gameon:
    print(check(user,comp))
