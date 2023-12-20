
import random
class Die:
    def __init__(self,size1,size2):
        self.size1=size1
        self.size2=size2
        self.roll1=1
        self.roll2=1
    def roll(self):
         self.roll1=random.randint(1,self.size1)
         self.roll2=random.randint(1,self.size2)
    def getValue1(self):
        return self.roll1
    def getValue2(self):
        return self.roll2
    def getFinalValue(self):
        return self.roll1+self.roll2
    def __str__(self):
        pass
    def __add__(self,other):
        self.roll+=other.roll
        return self.roll    
    def __gt__(self,other):
        return self.roll>other.roll
    def __eq__(self,other):
        return self.roll==other.roll
die1=Die(6,10)


class player(Die):
    def __init__(self,name):
        self.name=name
        self.size1=6
        self.size2=10
    def __str__(self):
        return self.name + ' has rolled a total of:'+str(self.roll1 + self.roll2)+'.'


class HighTwoGame(player):
    def __init__(self,pl1,pl2):
        self.name1=pl1
        self.name2=pl2
        self.pl1=player(pl1)
        self.pl2=player(pl2)
        self.size1=6
        self.size2=10
        self.total1=0
        self.total2=0
        pass
    def playOneGame(self):
        self.pl1.roll()
        self.pl2.roll()
        #return(self.pl1.getValue1(),self.pl1.getValue2(),self.pl1.getFinalValue(),' ,term2: ',self.pl2.getValue1(),self.pl2.getValue2(),self.pl2.getFinalValue())
        print(self.name1,'rolled',self.pl1.getValue1(),' and ',self.pl1.getValue2(),'so the total is ',self.pl1.getFinalValue())
        print(self.name2,'rolled',self.pl2.getValue1(),' and ',self.pl2.getValue2(),'so the total is ',self.pl2.getFinalValue())
        if self.pl1.getFinalValue()>self.pl2.getFinalValue():
            return self.name1+' wins!'
        elif self.pl1.getFinalValue()==self.pl2.getFinalValue():
            return 'Tie'
        elif self.pl1.getFinalValue()<self.pl2.getFinalValue():
            return self.name2+ ' wins!'
    def playManyGames(self,number):
        for x in range(number):
            self.pl1.roll()
            self.pl2.roll()
        #return(self.pl1.getValue1(),self.pl1.getValue2(),self.pl1.getFinalValue(),' ,term2: ',self.pl2.getValue1(),self.pl2.getValue2(),self.pl2.getFinalValue())
            print(self.name1,'rolled',self.pl1.getValue1(),' and ',self.pl1.getValue2(),'so the total is ',self.pl1.getFinalValue())
            print(self.name2,'rolled',self.pl2.getValue1(),' and ',self.pl2.getValue2(),'so the total is ',self.pl2.getFinalValue())
            self.total1+=self.pl1.getFinalValue()
            self.total2+=self.pl2.getFinalValue()
        print(self.name1,'total:',self.total1)
        print(self.name2,'total:',self.total2)
        if self.total1>self.total2:
            return self.name1+' wins!'
        elif self.total1==self.total2:
            return 'Tie'
        elif self.total1<self.total2:
            return self.name2+ ' wins!'


        