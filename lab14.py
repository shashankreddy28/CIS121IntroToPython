class Binomial:
    def __init__(self,x='x',y='y',n='n'):
        self.x=x
        self.y=y
        self.n=n
    def evaluate(self):
        try:
            sum1=0
            for k in range(0,self.n+1):
                coefficient=fact(self.n)//(fact(k)*fact(self.n-k))
                sum1+=coefficient*(self.x**k)*(self.y**(self.n-k))
            return int(sum1)
        except ValueError:
            return f'The values x,y,n must be integers'
        except TypeError:
            return f'The values x,y,n must be integers'
    def expand(self):
        try:
            sum1 = ''
            for k in range(0,self.n+1):
                coefficient=fact(self.n)//(fact(k)*fact(self.n-k))
                if k==0:
                    sum1+=f'{coefficient}({self.x}^{k})({self.y}^{self.n-k})'
                else:
                    sum1+=f' + {coefficient}({self.x}^{k})({self.y}^{self.n-k})'
            return sum1
        except ValueError:
            return f'The values x,y,n must be integers'
        except TypeError:
            return f'The values x,y,n must be integers'


    
    def __str__(self):
        return f'({self.x}+{self.y})^{self.n}'



def fact(number):
    if number==1 or number==0:
        return 1
    
    else:
        return number*fact(number-1)

Binomial1=Binomial(x=4,y=2,n=5)
print(Binomial())
print(Binomial1.evaluate())
print(Binomial1.expand())