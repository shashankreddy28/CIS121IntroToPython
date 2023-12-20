#from math import *
import math
import random
from functools import reduce
from string import punctuation
import turtle

print("Hello")
for x in range(10):
    print(x)
#hw q2 week2
"""x=int(input("Enter a number:"))
ans=((((x+2)*3)-6)/3)
print(ans,"is the answer")"""
#hw q3 week2
#power is takes place first, then the floor division and then product and sum
"""print(30-2**2+8//3**2*10)"""

#q4 week2
"""my_int=7
#my_int=my_int+3
my_int+=3
print(my_int)"""
#q5 week2
"""a=5
b=4
c=2
print(a//c,a%b,b**c,sep='\n')
b*=c
print(b)"""
#q6
"""num=int(input("Enter a number:"))
ans=num%2
print(ans)"""
#q7
"""month=input("Enter month:")
day=int(input("Enter day:"))
year=int(input("Enter year:"))
print(f"The date given is {month},{day},{year}.")"""
#q8
"""base=int(input("Enter the base:"))
base2=int(input("Enter the 2nd base:"))
height=int(input("Enter the height;"))
area=((base+base2)/2)*height
print("Area of trapizium is :",area)"""
#q9 end of HW week2
"""rad=radians(75)
#print(math.cos(rad))
b=math.sqrt((10**2+4**2)-((2*10*4)*(math.cos(rad))))
print(b,'is the length of b.')
z=(b**2+4**2-10**2)/(2*b*4)
#print(z)
angle=math.acos(z)
deg=degrees(angle)
print(deg)"""
#lab, week2
#q1
"""seconds=int(input("Enter the seconds:"))
minutes=seconds//60
seconds1=seconds%60
hours=minutes//60
minutes=minutes%60
print("hours:",hours,"minutes:",minutes,"seconds:",seconds1)"""
#q2
"""initial=334205119
seconds=1685720
birth=seconds//7
death=seconds//13
immi=seconds//35

totalpop=initial+birth+immi-death
print(totalpop,"is the population.")"""
#q3

"""seconds=int(input("Enter seconds since beggining of the year:"))
minutes=seconds//60
seconds1=seconds%60
hours=minutes//60
minutes=minutes%60
days=hours//24
hours=hours%24
print(days,"days",hours,"hours",minutes,"minutes",seconds1,"seconds","after the start of 2023")"""

#q4
"""population=334205119
x=((((((population+350)**2)-12)/50))**(1/5))
x1=round(x)
print("Average amount of flapjacks eaten is",x1)"""

#week3 hw
#q3
"""while True:
    lc=input("Enter light color('r':red,'y':yellow,'g':green):")
    if lc=='r':
        print("Stop!")
        break
    elif lc=='y':
        print("Yield")
        break
    elif lc=='g':
        print("Go!")
        break
    else:
        print("Wrong Input, Pls enter again:")"""

#q4
"""i=int(input("Enter your age:"))
a=input("Enter your athleticism goal(a:above average,b:below average):")
if i>=20 and i<=39:
    if a=='a':
        print("Your resting heart rate should be between 47-72.")
    if a=='b':
        print("Your resting heart rate should be between 73-93.")
if i>=40 and i<=59:
    if a=='a':
        print("Your restin heart rate should be between 46-71.")
    if a=='b':
        print("Your resting heart rate should be between 72-94.")
if i>=60 and i<=79:
    if a=='a':
        print("Your resting heart rate should be between 45-70.")
    if a=='b':
        print("Your resting heart rate should be between 71-97.")"""


#q5
"""a=int(input("Enter first number:"))
a1=int(input("Enter second number:"))
a2=int(input("Enter third number:"))
if a>=a1 and a>=a2:
    if a1>=a2:
        print(a2,a1,a)
    elif a2>=a1:
        print(a1,a2,a)
elif a1>=a and a1>=a2:
    if a>=a2:
        print(a2,a,a1)
    elif a2>=a:
        print(a,a2,a1)
elif a2>=a and a2>=a1:
    if a>=a1:
        print(a1,a,a2)
    elif a1>=a:
        print(a,a1,a2)"""








#q6
"""a=int(input("Enter first number:"))
a1=int(input("Enter second number:"))
a2=int(input("Enter third number:"))
if a>=a1 and a>=a2:
    if a1>=a2:
        print(a,a1,a2)
    elif a2>=a1:
        print(a,a2,a1)
elif a1>=a and a1>=a2:
    if a>=a2:
        print(a1,a,a2)
    elif a2>=a:
        print(a1,a2,a)
elif a2>=a and a2>=a1:
    if a>=a1:
        print(a2,a,a1)
    elif a1>=a:
        print(a2,a1,a)"""

#q7

"""numberOfTimes=int(input("Enter the number of times the coin flips:"))
for x in range(numberOfTimes):
    guess=input("Guess if the coin would flip heads or tails('H':heads , 'T':tails':")
    flip=random.randint(1,2)
    if flip==1:
        print('The coin flipped heads')
        if guess=='T':
            print('Unlucky, better luck next time')
        elif guess=='H':
            print('Good guess, you were right!')
    if flip==2:
        print("The coin flipped tails")
        if guess=='T':
            print("Good guess, you were right!")
        elif guess=='H':
            print("Unlucky, better luck next time")"""


#q8
# 1knut= 1/29 sickle ,,,,29knuts= 1 sickle
# 1 sickle= 1/17 galeon,,,, 17 sickle=1galeon
# 493 knuts= 1 galeon


"""knuts=int(input("Enter the number of knuts:"))
galeon=knuts//493
knuts=knuts%493
sickle=knuts//29
knuts=knuts%29
# if knuts!=0 and galeon!=0 and sickle!=0:
#     print('g:',galeon,'s:',sickle,'k:',knuts)
# elif knuts==0 and galeon==0:
#     print('s:',sickle)
# elif galeon==0 and sickle==0:
#     print('k:',knuts)
# elif sickle==0 and knuts==0:
#     print('g:',galeon,)
# elif knuts==0:
#     print('g:',galeon,'s:',sickle)
# elif sickle==0:
#     print('g:',galeon,'k:',knuts)
# elif galeon==0:
#     print('k:',knuts,'s:',sickle)
if galeon!=0:
    print(f'g:{galeon}',end=' ')
if sickle!=0:
    print(f's:{sickle}',end=' ')
if knuts !=0:
    print(f'k:{knuts}')"""




#week3 LAB
#q1
"""print(4==5)
print(4==4)"""
#q2 (a)
#using if
"""a=int(input("Enter a number:"))
if a%2==0:
    print("Even")"""
#q2(b)
"""a=int(input("Enter a number:"))
if a%2==0:
    print("Even")
else:
    print("Odd")"""

#q2(c)
"""a=int(input("Enter a number:"))
if a>=0:
    if a%2==0:
        print("The number entered is a positive even number")
    else:
        print("The number entered is a positive odd number")
else:
    print("The number entered has to be a positive integer")"""

#main question week3 lab

"""pos=input("Enter your post(j:junior,s:senior):")
sale=int(input("Enter the sales amount:"))
rate=0
nsale=0
if sale<=0:
    print("Please meet the HR")
r1mj=150
r2mj=1000
r3mj=5000

r1ms=200
r2ms=1250
r3ms=7000


if pos=='j':
    if sale<=5000:
        rate=0.03*sale
        print(rate)
    elif sale>=5001 and sale<=25000:
        rate=r1mj+((sale-5000)*0.04)
        print(rate)
    elif sale>=25001 and sale<=100000:
        rate=r1mj+r2mj+((sale-(25000))*0.05)
        print(rate)
    elif sale>=100000:
        rate=r1mj+r2mj+r3mj+((sale-(100000))*0.07)
        print(rate)
if pos=='s':


    if sale<=5000:
        rate=0.04*sale
        print(rate)
    elif sale>=5001 and sale<=25000:
        rate=r1ms+((sale-5000)*0.05)
        print(rate)
    elif sale>=25001 and sale<=100000:
        rate=r1ms+r2ms+((sale-(25000))*0.07)
        print(rate)
    elif sale>=100000:
        rate=r1ms+r2ms+r3ms+((sale-(100000))*0.1)
        print(rate)"""
    
#week4 mavpass
"""enter=input("Enter a string:")
lenter=list(enter)
n=1
if len(lenter)>=2:
    while n<=len(lenter):
        print(lenter[n-1],end='')
        n+=2"""



"""for a in range(1,21,2):
    print(a)"""

"""curpop=10000
rate=23
time=11*24*60*60
finalpop=curpop+(time*rate)
print(finalpop)"""    


"""for x in range(1,6):
    print(x*'*')"""
"""for s in range(1,11):
    print(s*2)"""

"""for x in range(1,11):
    for i in range(1,11):
        
        print(x*i,end=' ')
        if i==10:
            print('.')
    print(' ')#this is used so that we can have an wmpty line in between."""
        

"""pos=input("Enter your post(1:junior,2:senior):")
sale=int(input("Enter the sales amount:"))
rate=0
nsale=0
if sale<=0:
    print("Please meet the HR")
r1mj=300
r2mj=600


r1ms=450
r2ms=855



if pos=='1':
    if sale<=10000:
        rate=0.03*sale
        print(rate)
    elif sale>=10001 and sale<=15000:
        rate=r1mj+((sale-10000)*0.04)
        print(rate)
    elif sale>=15001 and sale<=25000:
        rate=r1mj+r2mj+((sale-(15000))*0.06)
        print(rate)
if pos=='2':


    if sale<=10000:
        rate=0.045*sale
        print(rate)
    elif sale>=10001 and sale<=15000:
        rate=r1ms+((sale-10000)*0.057)
        print(rate)
    elif sale>=15001 and sale<=25000:
        rate=r1ms+r2ms+((sale-(25000))*0.075)
        print(rate)"""
    

"""for x in range(50,102):
    if x%2==1:
        print(x)"""


"""for x in range(1,8):
    for i in range(1,x+1):
        print(i,end=' ')
    print("\b.")"""
    
    
#lab4:-
"""upper=int(input("Enter a prefered upper bound:"))
de=0
ab=0
per=0
devsum=0


print('Between 1 and',upper,'there are...')

for x in range(1,upper+1):
    devsum=0
    for i in range(1,x):
          if x%i==0:
               devsum+=i
    if devsum==x:
        per+=1
    if devsum<x:
        de+=1
    if devsum>x:
        ab+=1
                
                   
print(de,'deficient number')
print(per,'perfect number')
print(ab,'abundent number')"""




"""for i in range(5,0,-1):
    for j in range(i):
        print(j,end='')
    print()"""
"""word='alphabetical'
for x in [2,5,8,11]:
        print(word[x],end='')"""

"""word='alphabetical'
x=len(word)
for i in range(2,x,3):
    print(word[i],end='')"""



"""input_string = "alphabetical"
for char in input_string:
    if char == "a":
        print("p", end="")
    elif char == "b":
        print("b", end="")
    elif char == "l":
        print("i", end="")
    elif char == "h":
        print("l", end="")"""

"""i=1
while i<17:
    if i%2==0:
        print(i)
    i+=1"""
"""x=1
while True:
    if x**2<=12000:
        x+=1
    else:
        print(x)
        break"""
"""f=1
while f==1:
    a=int(input("Enter a number:"))
    for x in range(0,a+1):
        if x**2==a:
            print('perfect')
            f=2
        else:
            continue"""
    
        

"""for i in range(1,8):
    for j in range(1,i+1):
        print(j,end=' ')
    print()"""
"""print(type(2+5!=8))"""

"""variable='fly bird'
variable*=4
print(variable)"""


"""height=float(input("Enter height:"))
radius=float(input("Enter radius:"))
print((2*(22/7)*(radius**2))+(2*(22/7)*radius*height))"""

"""print('while loop')
x=1
while x<=10:
    print(2*x)
    x+=1
print('for loop')
for x in range(1,11):
    print(2*x)"""

"""
for x in range(1,4):
    for j in range(1,x+1):
        print('*',end='')
    print()"""
"""x=10
y=(x!=10)
print(y)"""
"""n=1
while True:
    if n**3>=15000:
        print(n-1)
        break
    else:
        n+=1
        continue"""
"""x=int(input("Enter number:"))
count=0
for i in range(x+1):
    count+=i
if count%i==0:
        print(count)"""


"""x=int(input("Enter number:"))
count=0
for i in range(1,x+1):
    count=0
    for j in range(1,i+1):
        count+=j
    print(count)
print()"""

"""x=int(input("Enter number:"))
count=0
for i in range(1,x+1):
    count=0
    for j in range(1,i+1):
        count+=j
    if count%i==0:
        print(count)
print()"""


#increasing triangle
"""for x in range(1,6):
    for i in range(1,x+1):
        print(i,end=' ')
    print()"""
"""for x in range(1,5):
    print('*' * x)"""

"""for x in range(1,6):
    print('*' * x)
for j in range(4,0,-1):
    print('*'*j)"""
"""a=1
while a<=9:
    print('*'* a)
    a+=2"""

"""k=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k+=1
    print()


k=65
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k+=1
    print()"""

"""k=65
for x in range(1,6):
    print(chr(k) * x)
    k+=1"""

"""k=65
for x in range(5,0,-1):
    for i in range(1,x+1):
        print(chr(k),end=' ')
    k+=1
    print()"""
        
#week5
#start prep form here
#opening file in python
#write mode
"""f=open("mypython.txt",'w')
a=f.write("First line."+'\n'+"second line."+'\n')
f.close ()"""

"""f=open('integer.txt','w')
for count in range(10):
    number = random.randint(1,10)#in randint func, upper bound and lower bound are included
    f.write(str(number)+'\n')
f.close()"""

#read mode

"""f=open('integer.txt','r')
a=f.read()
print(a)
f.close()"""

#read and prints a file
"""f=open('mypython.txt','r')
for line in f:
    print(line)

f.close()"""  
        
"""f=open('mypython.txt','r')
a=f.read()
print(a)
f.close()"""    

#adding all the numbers in a the file given that each number is on a new file!
"""f=open("integer.txt",'r')
thesum=0
for line in f :
    line=line.strip()
    number=int(line)
    thesum+=number
print("The sum is",thesum)
f.close()"""
#same as above
"""f=open("integer.txt",'r')
thesum=0
for line in f :
    thesum+=int(line)
print("The sum is",thesum)
f.close()"""

#enter numbers in same line with space in between
"""f=open('integer.txt','w')
for count in range(10):
    number = random.randint(1,10)#in randint func, upper bound and lower bound are included
    f.write(str(number))
    f.write(' ')
f.close()"""

#if numbers are in the same line find sum
"""f=open("integer.txt",'r')
thesum=0
for line in f:
    wordlist=line.split()
    for word in wordlist:
        number=int(word)
        thesum+=number
print('the sum is',thesum)
f.close()"""

#reads 1 line
"""f=open('mypython.txt','r')
a=f.readline()
print(a)

f.close()"""

#readslines gives string output
"""f=open('mypython.txt','r')
a=f.readlines()
print(a)

f.close()"""

# strings and substrings
"""x="Monty Python"
print(x[0])
print(x[-1])
print(x[len(x)-1])
print(x[:5])"""

"""s='what is your name?'
print(s[::2])#wa syu ae
print([2:8:-1])#error"""

#printing the alphabets
"""x='acegikmoqsuwy'
y='_bdfhjlnprtvxz'
for i in range(13):
    print(x[i]+y[i+1],end='')"""
"""
x='Alan Turning'
y=x[-1::-1]
print(y)
    
"""

#quiz 5
"""x='rest'
y='chair'
if len(x)>len(y):
    print(x)
else:
    print(y)
#b
z='helloo hello'
sp=z.split()
if len(sp[0])>len(sp[1]):
    print(sp[0])
else:
    print(sp[1])"""

#week 6
"""x=2

print([x,math.sqrt(x)])
print(x+1)

first=[1,2,3,4,5]
second=list(range(1,6))
print(first , second)
if first == second: #so we can compare lists
    print('they are the same')

third=list("Hi there")
print(third)
print(third[0])
print('1234')
print([1,2,3,4])# prints list
for number in [1,2,3,4]:
    print(number,end=' ')
print('')
print(3 in [1,2,3]) # check if something is present in the string, bool response
print(first+second+third)
print(first.append(1))#adding element to list
print(first)"""

# since list is mutable we can change any element of a  list
#concatnation
"""x=[1,2,3,4,5,6,8]
print('old list',x)
x[-1]=7
print('new list',x)"""

"""numbers=[2,3,4,5]
for index in range(len(numbers)):
    numbers[index]= numbers[index]**2
print(numbers)"""

#basic list functions
"""
yallo=['yallo']
word=['hi', 'there','hello']
for index in range(len(word)):
    word[index]=word[index].upper()
print(word)
word.insert(2,',')# insert uses (index, element) as the insert func!
print(word)
word.pop(2)# pop is used to pop element at the index, or if no value is gice then it will remove the last element of the list
print(word)
word.append('there')# adds element to the last of the list
print(word)
word.append(['there'])# we can use this to create a nested list
print(word)
word.extend(yallo)# used to add 2 lists together similar to concatinating lists
print(word)"""


#checking element in list
"""lista=[32,42,52]
target=52
if target in lista:
    print(lista.index(target))#index is used to give the first occurance of object.
else:
    print('it is not a part of the list')"""
    

#using sort to arrange list in asc or desc order
"""number=[4,3,8,9,6,5,10,4]
number.sort()#defaults as ascendending order
print(number)
number.reverse()#descending order
print(number)"""

# changing one list and the other one changes
"""first=[1,2,4]
second=first
first[2]=3
print(first,'first')
print(second,'second')# we see that bot the lists change
"""
# tuple
"""fruits=('apple','banana')
others=('fish','chicken')
food= fruits + others
print(food)
first=[1,2,4]
print(tuple(first))"""#change list to tuple

#week6 hw
#q1

"""l1=[]
for x in range(100):
    i=[0]
    l1.extend(i)
print(l1)
print('new list')
l2=[]
i=0
for x in range(100):
    i=0
    l2.append(i)
print(l2)"""


#dictionaries
"""
di={'hi':[2,3]}#list can have list as value in dict
print((di['hi'])[1])# we can print indivudual part of the list in the key too
"""

"""info={}
info["name"]='sandy'
info['b']='job'
info['job']="hacker"
print(info)
print(info['name'])
print(info['job'])
print(info)

if 'job' in info:#checking if the key exists and print the value
    print(info["job"])
if 'job' in info.keys():#same as above but checking in dict.keys() so that wit easier
    print(info["job"])
info.pop("job")#removing something from dict
print(info)

for key in info:
    print(key,info[key])#prints key and then values

print(info.items()) # prints key, value in the form of a tuple"""

#q1
"""x={} #x={'chips':10,'juice':20,'biscuits':30,'mango':40}
x["chips"]=10
x["juice"]=20
x["biscuits"]=30
x["mango"]=40
print(x)"""

#q2
"""
total=0
while True:
    a=input("Enter item name or type 'done' :")
    if a in x:
        j=int(input("Enter quantity of item:"))
        total+= (x[a])*j
    elif a=="done":
        break
print(total,'is the total price')"""
        
        
        
"""b=int(input("Enter the number of different items u want:"))#enter just numbr of different items, bought the total quantity
total=0
for i in range(b):
    a=input("Enter item name:")
    if a in x:
        j=int(input("Enter the number of the item:"))
        total+= (x[a])*j
print(total,'is your total')"""        
    
#week7
#def function
"""
def average(lyst):
    theSum=0
    for number in lyst:
        theSum+=number
    return theSum/len(lyst)

l=[1,2,3,4,5,6]
a=average(l)
print(a)


def f(x):
    return x**2
def g(x):
    return x**3
funcs=[f,g]
print(funcs[0](5),funcs[1](5),sep='\n')


def multiplication(n):
    return n*n
numbers=(1,2,3,4)
result=map(multiplication,numbers)#using map a higher level functions, APPLIES A FUNC TO EACH VALUE IN A FUNC its syntax is map(func,values)  values could be in the form of a list ot tuple or whatever too!  
print(list(result))
"""
# use of func:-
#abstraction which is the quality of dealing with ideas rather than events. Used to handle complexity by hiding unnecessary details
#eliminates redundancy
#reduces the chance of error
#hides complexity
#general method of systematic variation

"""
def summ(lower,upper):#ig it includes the upper limit.
    if lower>upper:
        return 0
    else:
        return lower + summ(lower+1,upper)
print(summ(2,5))
"""

#fibonacci sequence
# 1 1 2 3 5 8 13

#recursive definition of the nth fibonacci number
#fib(n)= 1, when n=1 or n=2
#fib(n)=fib(n-1) + fib(n-2) , for all n>2


def hi(n):
    if n<3:
        return 1
    else:
        return hi(n-1)+hi(n-2)

print(hi(3))# prints the number at that index in the fibonacci sequence


def sum(n):
    print(n)

sum(20)
"""f=abs
print(f)
print(f(-4))
"""

"""
funcs=[abs,math.sqrt]
print(funcs[1](4))
"""
"""
words=["231",'20','-45','99']
map(int,words)
print(words)
words=list(map(int,words))
print(words)
"""
"""
def odd(n):
    return n%2==1
odd_number=list(filter(odd,range(10)))#use of filter inbuilt func, need to find out what it does

"""
#from functools import reduce
#import was used for this
"""
def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
data =[1,2,3,4]
print(reduce(add,data))#find out how reduce func works
print(reduce(multiply,data))

#using lambda func
data=[1,2,3,4]
sum1=reduce(lambda x,y:x+y,data)
print(sum1)
"""





#week7 hw
"""def MyFctn(number):
    total = 0
    while number > 0:
        total += number * (number - 1)
        number -= 1
    return total
print(MyFctn(5))"""
#ans is 40=(5*4)+(4*3)+(3*2)+(2*1)+(1*0)

"""
def Nf():
    number=1.0
    total=0
    while number<100:
        total = 1//number
        number += 1
        return total
print(Nf())"""
#ans =1.0

#q3
"""
def member(price):
    price=(85/100)*price #85 since the mothers day discount is also added
    return price

def notmember(price1):
    price1=(95/100)*price1 # only mothers day discount
    return price1
a=int(input("Enter the amount of the item:"))
b=(input("Are you a member (y:yes, n:no):"))
if b=='y':
    print(member(a),'is your total amount as you are a member.')
if b=='n':
    print(notmember(a),'is your total amount as you are not a member.')

 """
#q4
"""
def cm(x,y,z):
    l1=[]
    if y>=x:
        for i in range(y,z+1):
            if i%x==0 and i%y==0:
                l1.append(i)
    if x>y:
        for i in range(x,z+1):
            if i%x==0 and i%y==0:
                l1.append(i)
    return(l1)
        
a=int(input("Enter first number to find multiple of"))
b=int(input("Enter second number to find multiple of"))
c=int(input("Enter upper limit:"))

new=cm(a,b,c)
for j in new:
    print(j)
"""

#q6
"""
def check(a,b):
    str1=''
    if len(a)>=len(b):
        for x in range(len(b)):
            if a[x]==b[x]:
                str1=str1+a[x]
    if len(b)>len(a):
        for x in range(len(a)):
            if a[x]==b[x]:
                str1=str1+a[x]
    return str1
s=input("Enter first word:")
s1=input("Enter second word:")
print(check(s,s1))
"""
#q5
"""
def sort(list):
    return list == sorted(list)
list1 = []
while True:
    a = input("Enter a number and type 'done' if you are done: ")
    if a == 'done':
        break
    else:
        list1.append(int(a))
print(list1)
print (sort(list1))
"""
#hw2
"""
def func(a,b,c):
    while True:
        
        if a.isnumeric():
            a=int(a)
        else:
            print(a,"is not a number")
            break
        if b.isnumeric():
            b=int(b)
        else:
            print(b,"is not a number")
            break
        if c.isnumeric():
            c=int(c)
        else:
            z=c+" is not a number"
            return z
            break
        
        if a==0 or b==0:
            return "A zero can not be devided, wrong input"
        else:
            x=a/b
            y=x+c
            return y
            break

x1=(input("Enter first number:"))
x2=(input("Enter second number:"))
x3=(input("Enter third number:"))
print(func(x1,x2,x3))          
"""
#exam 2 prep:-
# creating a dict, changing values and deleting pairs
#print("Hello world")

"""d={'a':100,'b':200,'c':300}
d['a']=400
print(d)
del d['a']
print(d)"""

"""rand_num= random.randint(1,5) # remember, randint counts the upper limit too!!
for i in range(6):
    print("hello"*rand_num)"""

"""
for i in range(6):
    rand_num= random.randint(1,5)
    print("hello"*rand_num)"""

#game:-
'''
questions=['What is the capital of France?','Which state has only one neighbor?']

answers=['Paris','Maine']
num_right=0
for i in range(len(questions)):
    guess=input(questions[i])

    if guess.lower()== answers[i].lower():
        print("Correct")
        num_right+=1
    else:
        print("Wrong. The answer is", answers[i])
    print('you have',num_right,'out of', i+1,'right.')'''

#funcs practice
"""
def multiple_print(string,n):
    return(string*n)
print(multiple_print("Heyy",10))"""

#append and write will create a new file, even a+(append and read) 
"""
z=open('mypython.txt','a+')
a=z.write('hello')
z.seek(0)
b=z.readline(6)
print(b)
z.close()"""

"""  
x=open('myfile12.txt','a+')
a=x.write('Hello world!')
x.close()"""

"""
week=['sun','mn','t','wed']
print(week[-3:-1])"""

"""
student={'name':'alex','class':'Cis','marks':88}
print(student['marks'])
del student['marks']
print(student)
"""
#update is used iin dict to updTE THE VALUE OF A KEY OR ADD THE KEY VALUE PAIR IF THEY DOTN EXIST
"""

d={0:10,2:20}
d.update({2:30})
print(d)"""

#join is used to join everythig in list to srting using what is given , of in bw the string itself
#replace is used to replace a specific term in the string
'''s=["hi","there!"]
z=(' '.join(s))
print(z)
a=''.join(z)
print(a)
x=a.replace('i','o')
print(x)'''



#mavpass questions
"""
f=open('mypython.txt','r')
a=f.read()
f.close()
"""

#2
"""
l=[]
y=0
f=open('mypython.txt','r')
lines=f.readlines()
f.seek(0)
for x in range(len(lines)):
    y=f.readline()
    l.append(y)
print(l)
"""
#q2 week5 ws , the fileis deleted pls create again
"""f=open('thisfile.txt','r')
z=open("thatfile.txt",'w')

count=2
for x in range(13):
    a=f.readline()
    if count%2==0:
        z.write(str(a))
    count+=1
f.close()
z.close()
"""
#prints alternative lines
"""f=open('thisfile.txt','r')
z=open("thatfile.txt",'w')
a=f.readlines()
for x in range(len(a)):
    if x%2==0:
        z.write(a[x])

f.close()
z.close()"""
    
#q5 week 5 ws

"""f=open('integer.txt','r')
z=open('myfile.txt','w')

a=f.read()
word=a.split()
for x in range(len(word)):
    l=''

    if x%5==0:
        z.write("\n")
        l=l+' '+word[x]
        z.write(l)
    else:
        l=l+' '+word[x]
        z.write(l)"""

#week 6 hw

"""mydict={'a':10,'c':30, 'b':20}
dict1={}
print(mydict['b'])
for x in mydict:
    if mydict[x]==30:
        print(x)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(sorted(mydict.items()))
a=sorted(mydict.values())
x={'hi':20,'a':25}
mydict.update(x)

print(mydict)
print(a)"""

#q4
"""dict1={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
a= input("enter a number;")
for x in a:
    print(dict1[x],end=' ')
"""
"""list1=[1,2,3,4,5,6]
for x in range(len(list1)):
    list1[x]= list1[x] +3
print(list1)"""

"""list1=[1,2,3,4,5,6]
for x in list1:
    if x%2==0:
        list1.remove(x)
print(list1)"""

"""list1=[1,2,3,4,-1,-2,-3,-4]
for s in range(len(list1)):
    if list1[s]>=0:
        continue
    else:
        list1[s]=abs(list1[s])
print(list1)"""

"""f=open('file1.txt','w')
for x in range(100):
    a=random.randint(0,10)
    f.write(str(a))
    f.write('\n')
f.close()

r=open('file1.txt','r')
r1=r.readlines()
sum1=0
for x in r1:
    x=x.strip()
    x=int(x)
    sum1+=x
print(sum1/len(r1))"""

"""x=[1,2,3,4,5]
print(min(x))"""

"""def func1(a,b):
    l1=[]
    for x in range(100):
        if x%a==0 and x%b==0:
            l1.append(x)
    return(l1)
a=func1(2,3)
for y in a:
    print(y)"""

"""def check(a):
    if a == sorted(a):
        return True
    else:
        return False"""     



"""def func2(a):
    y=sorted(a)
    if a==y:
        return True
    else:
        return False
      

print(func2([1,2,3,4]))"""


"""def func1(a):
    d={'even':[],'odd':[]}
    for x in a:
        if x%2==0:
            d['even'].append(x)
        else:
            d['odd'].append(x)

    return(d)
a=func1([1,2,3,4,5,6,7])
print(a)
#method1
f=open('file1.txt','w')
f.write('even:')
for i in a['even']:
    f.write(str(i)+' ')
f.write('\n'+'odd:')
for j in a['odd']:
    f.write(str(j)+' ')
f.close()
#method2
f.write('even'+' '.join(map(str,a['even']))+'\n')
f.write('odd'+' '.join(map(str,a['odd']))+'\n')
f.close()"""

"""a='Hi hello look bbc news'
x=''.join(a)
print(x)
a1=['hi','hello','look','bbc','news']
a2=[1,2,3,4,5]
z=' '.join(a1)
z1=(' '.join(map(str,a2)))
print(z)
print(z1)"""

"""a=[1,2,3,4,-1,-2,-3]
count=0
for s in a:
    count+=1
    if s>=0:
        continue
    else:
        a[count-1]=abs(s)
print(a)"""

"""a={'de':3,'ab':2,'bc':1}
x=(sorted(a.keys()))
for i in x:
    print(i)"""

"""f=open('file1.txt','r')
lines=0
for line in f:
    lines+=1
f.seek(0)
c=0
for x in range(lines):
    
    a=f.readline()
    z=a.split()
    b=int(z[1])
    c+=b
print(c)"""

"""a='caal daq'
dict1={'c':'g','a':'o','l':'d','d':'j','q':'b'}
b=''
for x in a:
    if x in dict1:
        b = b+ dict1[x]
    else:
        b= b+x
print(b)"""


"""def factorial(n):
    if n==0 or n==1:
        return(1)
    else:
        fact=n*factorial(n-1) 

    return(fact)  
print(factorial(5))"""


"""dict1={'c':1,'b':2,'a':3}
c=sorted(dict1.items())
print(c)"""

#way to sort a list, we cant initialise the list.sort to a variable, only the original list gets  edited
"""numbers=[3,5,2,1]
numbers.sort()
print(numbers)"""


#random.choice is used to get random element from list
"""names=["joe","Bob",'Sue']
player= random.choice(names)
print(player)"""

#random.sample picks random from list and adds to another list, if the 2nd argumetn is the len of th list then the list is shuffeled and is assigned to the new variable
"""names=["joe","Bob",'Sue']
team=random.sample(names,2)
print(team)"""

#using random.shuffle
"""names=["joe","Bob",'Sue']
random.shuffle(names)
for x in names:
    print(x)"""

#this code replaces punctuation
#this need the import func mentioned above : from srting import punctuation

"""s="Hi! This is a test"
print(s.split())


for c in punctuation:
    s=s.replace(c,' ')
print(s)"""

#prints the puctuations in the string
"""
s="Hi! This is a test"
print(s.split())
from string import punctuation
for c in punctuation:
    if c in s:
        print(c)"""

# checks for the number of time a word is repeated in a string
"""s=input('enter a string:')
for c in punctuation:
    s=s.replace(c,'')
s=s.lower()
l=s.split()

word=input("Enter a word:")
word=word.lower()
print(word,'appears',l.count(word),'times')"""


"""temp=0
while temp!=-1000:
    temp=eval(input("enter a temp or -1000 to exit out of the loop:"))
    if temp !=-1000:
        a=9/5*temp+32
        print('In faranheit',a)
    else:
        print('bye')"""

#multiple lines of code in 1 line
"""lines=[line.strip() for line in open('file1.txt','r').readlines()]
print(lines)"""

#this code can take the input as a number with commas 
"""a=input("Enter a number(this is hoping that the number has commas in it):")
for x in punctuation:
    if x in a:
        a=a.replace(x,'')
a=int(a.strip())
s=a+4000
print(s)"""

"""import random
l_points=0
m_points=0
for x in range (9):
    z=random.randint(1,199)
    if z==110:
        print('110 was generated so the game is over')
        break
    elif z%9==0:
        if (z/9)%2==0:
            print('no one gets a point! since number was',z)
            continue
    elif z%2==0:
        l_points+=1
        print('L got a point and is at',l_points,'points','since the number was ',z)
    elif z%2!=0:
        m_points+=1
        print("M got a point and has",'m_points,since the number was',z)

print('l has ',l_points, 'points')
print('m has ',m_points,'points')"""


#lab8

"""groceryList=[]
costOfItem=[]
qty=[]
while True:
    a=input("Enter your grocery list item:")
    if a.upper()=='DONE':
        break
    b=int(input("Enter cost of the item:"))
    c=int(input("Enter its quantity:"))
    groceryList.append(a)
    costOfItem.append(b)
    qty.append(c)
print(groceryList)
print(costOfItem)
dict1={}
for x in range(len(groceryList)):
    dict1.update({groceryList[x]:costOfItem[x]})
print(dict1)
total=sum(costOfItem)
print(total,'is the total price of the bill.')
dict2={'apple':10,'banana':15,'bread':20,'juice':25}

def check(fd,sd):
    aq=fd.items()
    bq=sd.items()
    print(aq)
    print(bq)
    if aq==bq:
        return('yes')
    else:
        return('no')

def check1(fdict,sdict):
    for i in fdict:
        if i in sdict:
            if fdict[i]>sdict[i]:
                print(i,'is cheaper in second dictionary')
            elif fdict[i]<sdict[i]:
                print(i,'is cheaper in first dictionary')
            else:
                print(i,'has the same price in both dicts')
        elif i not in sdict:
            print(i,'is only in dict1')
    for i in sdict:
        if i not in fdict:
            print(i,'is only in dict2')

for l in range(len(groceryList)):
    if qty[l]>1:
        print('Purchase',qty[l],groceryList[l]+'s','at cost',costOfItem[l],'dollars each')
    if qty[l]==1:
        print('Purchase',qty[l],groceryList[l],'at cost',costOfItem[l],'dollars each')

"""

#week9

#factorial using recursions
"""def factorial(n):
    if n ==1:
        return 1
    else:
        return(n*factorial(n-1))
num=int(input("Enter a number:"))
print("The factorial of",num,"is",factorial(num))"""

#recursion
"""def countDownAndUp(num):
    #print(num)
    if num==0:
        print('Reached the base case')
    else:
        countDownAndUp(num-1)
        print(num)  #here we dont reach the print statement till the end as we go back into the func , which is why it prints the base statement first 
countDownAndUp(4)
"""

#lab9

"""l1=[]
f=open('neww.txt','r')
a=f.readlines()
f.seek(0)
for x in range(len(a)):
    b=f.readline()
    b=b.strip()
    if b.isnumeric():
        l1.append(int(b))
print(l1)



def findMinimum(l):
    if len(l) == 0:
       raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l) == 1:
       return l[0]
    else:
       minNumber = findMinimum(l[1:])
       min1 = l[0]
       if minNumber < min1:
            min1 = minNumber
       return min1

def findMax(l2):
    if len(l2) == 0:
       raise ValueError('Cannot find the minimum of an empty list.')
    elif len(l2) == 1:
       return l2[0]
    else:
       maxNumber = findMax(l2[1:])
       max1 = l2[0]
       if maxNumber > max1:
            max1 = maxNumber
       return max1

def Extrema(list1,mina=True,maxa=True):
    if mina==False:    
        if maxa ==False:
            return None
        return findMax(list1)
    
    else:
        maxnmin=('max:', str(findMax(list1)),' ,min: ' ,str(findMinimum(list1)))
        return maxnmin 

print(Extrema(l1))
print(Extrema(l1,False,False))
print(Extrema(l1,False))"""


#week10
#func
#a function packages an algorithm in a single operation that can be called by name.
#to get inside the func you must view the code contained in its definition

#object
#object packages (single entity referance with a name)
# 1)set of data 2)its state 3)set of operations 4) its methods 
#this makes an object a more complex abstraction than a function.
#to get inside of an object you must view the code contained by its class.

#class definition is like a blueprint for each of the objects of that class. the blueprint contains:
#definition of fall the metods that its objects recognize.
#description of the data structures used to maintain the state of an object or its atttributes from the implementors point of view.

# a class is a template for objects.
#it contains the code for ll object methods.
# a func in a class is called methods

#creating class
"""class example:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add (self):
        return self.a+self.b
    
e=example(8,6)
print(e.add())"""
    

"""class enemy:
    def __init__(self,name,health,location):
        self.name=name
        self.health=health
        self.location=location
    def setname(self,name1):
        self.name=name1
    def getname(self):
        return self.name
    def gethealth(self):
        return self.health
    def getlocation(self):
        return self.location

e=enemy('Bro','100%','city')
a=input("Enter new name:")
e.setname(a)
print('Enemy details:',e.getname(),e.gethealth(),e.getlocation())"""


#week 11

#the data of a string object is actual character that make up that sting.

#from string import punctuation
"""class Analyser:
    def __init__(self,s):
        for c in punctuation:
            s=s.replace(c,' ')
            s=s.lower()
            self.words=s.split()
    def NumberOfWords(self):
        return len(self.words)

word='Hi hello look bbc news , on friday night . Heloooo' # if we dont use the replace func, the code counts the commas and fullstops too.
z=Analyser(word)
print(z.NumberOfWords())"""

#in oop(object oriented programming): the re are public and private variables
#public:accessible to anyone
#private:only accessible to methods within class
#in python generally variables are public

#general convention:
#those u want to be private: name them '_var1'(starting with an underscore)
#just to let others know that this variable in class should not be touched

#inheritance: when a class is built off another class
#the new class gets all of the methods and variables from the base class
#it can then provide new additional variables and methods
#it can overide methods from base class too    


"""class parent:
    def __init__(self,a) :
        self.a=a
    def method1(self):
        return self.a*2
    def method2(self):
        return self.a+'!!!'
class child(parent):
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def method1(self):
        return self.a*7
    def method3(self):
        return self.a+self.b
p=parent('Hi')
c=child('hi','bye')
print('Parent method1: ',p.method1())
print('parent method2: ',p.method2())
print()
print('Child method1: ', c.method1())#overide example
print('Child method2: ', c.method2())#inheriting methods
print('Child method3: ', c.method3())"""

"""class parent:
    def __init__(self,a) :
        self.a=a
    def print_var(self):
        print("The value of this class's variables are: ")
        print(self.a)

class child:
    def __init__(self,a,b) :
        parent.__init__(self,a)
        self.b=b
    def print_var(self):
        parent.print_var(self)
        print(self.b)
x=parent('Hello')
y=child('bro','ther')
x.print_var()
y.print_var()"""

"""class card:
    def __init__(self,value,suit) :
        self.value=value
        self.suit=suit
    def __str__(self):
        names=['Jack','Queen','King','Ace']
        if self.value<=10:
            return '{} of {}'.format(self.value,self.suit)
        else:
            return '{} of {}'.format(names[self.value-11],self.suit)
class CardGroup:
    def __init__(self,cards=[]):
        self.cards= cards
    def nextCard(self):
        return self.cards.pop(0)
    def hasCard(self):
        return len(self.cards)>0
    def size(self):
        return len(self.cards)
    def shuffle():
        return random.shuffle(self.cards) 
class StandardDeck(CardGroup):
    def __init__(self):
        self.cards=[]
        for s in ['Hearts','Diamonds','Clubs','Spades']:
            for v in range(2,15):
                self.cards.append(card(v,s))

a=StandardDeck()
print(a)"""

#lab11
"""class vector:
    def __init__ (self,x1,y1):
        self.x1=x1
        self.y1=y1
    def __str__(self):
         return "v="+str(self.x1)+'a'+'+'+str(self.y1)+'b'
    def __add__(self,other):
        return vector(self.x1 + other.x1,self.y1+other.y1)

vec=vector(1,2)
vec2=vector(3,4)
vec3=vec+vec2
print('1st vector: ',vec)
print('2nd vector: ',vec2)
print('sum: ',vec3)"""


# users1=[]
# passwords1=[]
# usersDict1={}

# userlist=['Bro']
# passwordlist=['pass']
# usersDictMain={'Bro':'pass'}

# f1=open('users.txt','a+')
# f1.seek(0)
# f2=open('password.txt','a+')

# class prog:
#     def CreateNewUser():
#         while True:
#             NewUser=input("Enter your new username:")
#             for hi in f1.readlines():
#                 hi=hi.strip()
#                 if NewUser==hi:
#                     print('Username already Exists!')
#             else:
#                 users1.append(NewUser)
#                 while True:
#                     NewPassword=input("Enter new Password:")
#                     NewPasswordCheck=input("Reconfirm Password:")
#                     if NewPassword == NewPasswordCheck:
#                         passwords1.append(NewPassword)
#                         usersDict1[NewUser]=NewPassword
#                         break
#                     else:
#                         print('Retry!')
#             print('account has been created successfully!')
#             break
#         for x in usersDict1.keys():
#             print(x)
#             f1.write(x+'\n')
#         for l in usersDict1.values():
#             print(l)
#             f2.write(l+'\n')

#     f1.seek(0)
#     f2.seek(0)

#     userlist=['Bro']
#     passwordlist=['pass']
#     usersDictMain={'Bro':'pass'}

#     def initialize():
#         a=f1.readlines()
#         for i in a:
#             z=i.strip()
#             userlist.append(z)
#         b=f2.readlines()
#         for j in b:
#             z1=j.strip()
#             passwordlist.append(z1)
#         count=0
#         for i in userlist:
#             usersDictMain[i]=passwordlist[count]
#             count+=1
#         for h in usersDict1:
#             usersDictMain[h]=usersDict1[h]
#         f1.seek=0
#         f2.seek=0
#     def login():
#         while True:
#             oldUserName=input("Enter your user name:")
#             if oldUserName in usersDictMain:
#                 oldPassword=input("Enter Old password:")
#                 if oldPassword == usersDictMain[oldUserName]:
#                     print('login complete!')
#                     break
#                 else:
#                     print('wrong password!, try again')
#             else:
#                 print('wrong username,try again!')


# # initialize()

# am=prog
# am.initialize()
# check=input('Do you aready have an account?(y/n):')
# if check.lower()=='y':
#     am.initialize()
#     am.login()
# else:
#     am.CreateNewUser()
#     am.initialize()



# f1.close()
# f2.close()


# print('for my referance.')
# print(userlist)
# print(passwordlist)
# print(usersDictMain)
# print(usersDict1)






# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return f"{self.username}:{self.password}"


# def save_to_file(filename, data):
#     f=open(filename, "a")
#     f.write(data + "\n")


# def create_account():
#     username = input("Enter a username: ")
#     password = input("Enter a password: ")

#     user = User(username, password)
#     save_to_file("usernames.txt", user.username)
#     save_to_file("passwords.txt", user.password)

#     print("Account created successfully!")


# def login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     f=open("usernames.txt",'r') 
#     usernames = f.read().splitlines()

#     f1=open("passwords.txt",'r')
#     passwords = f.read().splitlines()

#     if username in usernames and password in passwords:
#         print("Login successful!")
#     else:
#         print("Invalid username or password.")


# def main():
#     has_account = input("Do you have an account? (y/n): ")

#     if has_account.lower() == "n":
#         create_account()
#     else:
#         login()

# if __name__ == "__main__":
#     main()


#Comp Proj

"""
# Define a class to represent a User
class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return f"Name: {self.name}\nUsername: {self.username}\nPassword: {self.password}"

# Function to save data to a file
def save_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")

# Function to create a new user account
def create_account():
    users = [] # list to store all users' data
    while True:
        name = input("Enter your name: ")
        if name.strip():
            break
        print("Name cannot be empty.")
    while True:
        username = input("Enter a username: ")
        if username.strip():
            break
        print("Username cannot be empty.")
    while True:
        password = input("Enter a password (min. 5 characters): ")
        if len(password) >= 5:
            break
        print("Password must be at least 5 characters long.")

    user = User(name, username, password) # create a new User object
    save_to_file("usernames.txt", user.username) # save username to file
    save_to_file("passwords.txt", user.password) # save password to file
    save_to_file("names.txt", user.name) # save name to file

    # create a dictionary to store user data and append to list
    users_dict = {"name": name, "username": username, "password": password}
    users.append(users_dict)

    print("Account created successfully!")
    return users # return list of all users' data

# Function for user login
def login():
    users = [] # list to store all users' data

    # read data from files and create a list of dictionaries containing all users' data
    with open("usernames.txt") as f:
        usernames = f.read().splitlines()

    with open("passwords.txt") as f:
        passwords = f.read().splitlines()

    with open("names.txt") as f:
        names = f.read().splitlines()

    for i in range(len(usernames)):
        users_dict = {"name": names[i], "username": usernames[i], "password": passwords[i]}
        users.append(users_dict)

    # get username and password from user input
    while True:
        username = input("Enter your username: ")
        if username.strip():
            break
        print("Username cannot be empty.")
    while True:
        password = input("Enter your password: ")
        if len(password) >= 5:
            break
        print("Password must be at least 5 characters long.")

    # iterate through list of users' data and check if entered username and password match any stored user data
    for user in users:
        if user["username"] == username and user["password"] == password:
            user_obj = User(user["name"], user["username"], user["password"]) # create a new User object for the logged in user
            print(user_obj) # print the user's data
            return
    print("Invalid username or password.")

# Main function to handle program flow
def main():
    has_account = input("Do you have an account? (y/n): ")

    if has_account.lower() == "n":
        create_account()
    else:
        login()

if __name__ == "__main__":
    main()"""


# week 13


# a=0
# b=0
# dict1={}
# def mode(list1):
#     a=0
#     b=0
#     for x in list1:
#         if x in dict1:
#             dict1[x]+=1
#         else:
#             dict1[x]=1
#     return dict1
    
   
   
   
#     # a=dict1.values()
#     # b=dict1.keys()
#     # amax=max(a)
#     # bmax=


#     # a=max(dict1.values())
#     # return dict1.values().index(100)

# z=print(mode([1,2,3,4,1,5,1,6,1]))

# def revlist(list1):
#     list2=[]
#     for x in range(-1,-(len(list1)),-1):
#         list2.append(list1[x])
#     list2.append(list1[0])
#     return list2

# print(revlist([10,9,8,7,6,5,4,3,2,1]))


# x='toot'
# x1=x[::-1]
# print(x1)
# if x==x1:
#     print('T')
# else:
#     print('F')



# def even(n):
#     list1=[]
#     for x in n:
#         if x%2==0:
#             list1.append(x)
#     list1.sort()
#     print(list1)
# even([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])

# class rect:
#     def __init__(self,len:float,bre:float):
#         self.len=len
#         self.bre=bre
#     def getarea(self):
#         return self.len*self.bre
#     def getperi(self):
#         return 2*(self.len+self.bre)
#     def is_square(self):
#         if self.len==self.bre:
#             return True
#         else:
#             return False
# class square(rect):
#     def __init__(self,side):
#         self.side=side
#         rect.__init__(self,side,side)

# a=rect(2.0,2.0)
# print(a.getarea())
# print(a.getperi())
# print(a.is_square())
# sq=square(3)
# print(sq.getarea())
# print(sq.getperi())
# print(sq.is_square())

# class A:
#    def __str__(self):
#        return '1'
# class B(A):
#    def __init__(self):
#        super().__init__()
# class C(B):
#    def __init__(self):
#        super().__init__()
# def main():
#    obj1 = B()
#    obj2 = A()
#    obj3 = C()
#    print(type(obj1))
#    print(obj1, obj2,obj3)


# main()




# t=turtle.Turtle()
# t.width(2)
# t.left(90)
# t.forward(30)
# t.pencolor("red")
# t.setheading(0)
# t.forward(10)
# t.left(180)
# t.forward(20)
# t.hideturtle()

    



# # Define a class to represent a User
# class User:
#     def __init__(self, name, username, password):
#         self.name = name
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return f"Name: {self.name}\nUsername: {self.username}\nPassword: {self.password}"

# # Function to save data to a file
# def save_to_file(filename, data):
#     with open(filename, "a") as f:
#         f.write(data + "\n")

# # Function to create a new user account
# def create_account():
#     users = [] # list to store all users' data
#     while True:
#         name = input("Enter your name: ")
#         if name.strip():
#             break
#         print("Name cannot be empty.")
#     while True:
#         username = input("Enter a username: ")
#         if username.strip():
#             break
#         print("Username cannot be empty.")
#     while True:
#         password = input("Enter a password (min. 5 characters): ")
#         if len(password) >= 5:
#             break
#         print("Password must be at least 5 characters long.")

#     user = User(name, username, password) # create a new User object
#     save_to_file("usernames.txt", user.username) # save username to file
#     save_to_file("passwords.txt", user.password) # save password to file
#     save_to_file("names.txt", user.name) # save name to file

#     # create a dictionary to store user data and append to list
#     users_dict = {"name": name, "username": username, "password": password}
#     users.append(users_dict)

#     print("Account created successfully!")
#     return users # return list of all users' data

# # Function for user login
# def login():
#     users = [] # list to store all users' data

#     # read data from files and create a list of dictionaries containing all users' data
#     with open("usernames.txt") as f:
#         usernames = f.read().splitlines()

#     with open("passwords.txt") as f:
#         passwords = f.read().splitlines()

#     with open("names.txt") as f:
#         names = f.read().splitlines()

#     for i in range(len(usernames)):
#         users_dict = {"name": names[i], "username": usernames[i], "password": passwords[i]}
#         users.append(users_dict)

#     # get username and password from user input
#     while True:
#         username = input("Enter your username: ")
#         if username.strip():
#             break
#         print("Username cannot be empty.")
#     while True:
#         password = input("Enter your password: ")
#         if len(password) >= 5:
#             break
#         print("Password must be at least 5 characters long.")

#     # iterate through list of users' data and check if entered username and password match any stored user data
#     for user in users:
#         if user["username"] == username and user["password"] == password:
#             user_obj = User(user["name"], user["username"], user["password"]) # create a new User object for the logged in user
#             print(user_obj) # print the user's data
#             return
#     print("Invalid username or password.")

# # Main function to handle program flow
# def main():
#     has_account = input("Do you have an account? (y/n): ")

#     if has_account.lower() == "n":
#         create_account()
#     else:
#         login()

# if __name__ == "__main__":
#     main()





# class Vehicle:
#     def __init__(self,make, model,year,VIN,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.VIN=VIN
#         self.price=price
#     def get_make(self):
#         return self.make
#     def get_model(self):
#         return self.model
#     def get_year(self):
#         return self.year
#     def get_VIN(self):
#         return self.VIN
#     def get_price(self):
#         return self.price
    

#     def set_make(self,newmake):
#         self.make=newmake
#     def set_model(self,newmodel):
#         self.model=newmodel
#     def set_year(self,newyear):
#         self.year=newyear
#     def set_VIN(self,newVIN):
#         self.VIN=newVIN
#     def set_price(self,newprice):
#         self.price=newprice
    

#     def display_details(self):
#         return 'make: '+self.make+'\t model: '+self.model+'\t year: '+str(self.year)+'\t VIN: '+self.VIN+'\t price: '+str(self.price)
        
# class Car(Vehicle):
#     def __init__(self, make, model, year, VIN, price,doors,fuel):
#         super().__init__(make, model, year, VIN, price)
#         self.doors=doors
#         self.fuel=fuel
#         self.tax=10
#     def get_doors(self):
#         return self.doors
#     def get_fuel(self):
#         return self.fuel
    
    
#     def total_cost_car(self):
#         self.price=self.price+self.tax
    
#     def set_doors(self,newdoors):
#         self.doors=newdoors
#     def set_fuel(self,newfuel):
#         self.fuel=newfuel
    
#     def display_details(self):
        
#         return super().display_details()+'\t  doors: '+str(self.doors)+'\t fuel_type: '+self.fuel


# class Truck(Vehicle):

#     def __init__(self, make, model, year, VIN, price,cargo_capacity,towing_capacity):
#         super().__init__(make, model, year, VIN, price)
#         self.cargo_capacity=cargo_capacity
#         self.towing_capacity=towing_capacity
#     def get_cargo(self):
#         return self.cargo_capacity
#     def get_towing(self):
#         return self.towing_capacity
    
#     def set_cargo(self,newcargo_capacity):
#         self.cargo_capacity=newcargo_capacity
#     def set_towing(self,newtowing_capacity):
#         self.towing_capacity=newtowing_capacity
    
#     def display_details(self):
#         return super().display_details()+'\t cargo_capacity: '+str(self.cargo_capacity)+'\t towing_capacity: '+str(self.towing_capacity)


# class Motorcycle(Vehicle):

#     def __init__(self, make, model, year, VIN, price):
#         super().__init__(make, model, year, VIN, price)


# class VehicleInventory:

#     def __init__(self):
#         self.list1=[]
#     def add_vehicle(self,vehicle_object):
#         self.list1.append(vehicle_object)
#     def remove_vehicle(self):
#         self.list1.pop()
#     def display_all(self):
#         for x in self.list1:
#             print(x.display_details())





# car1=Car('make_of_car','model_of_car' , 2000, 'QWERTY123', 100,4,'pertol')
# car2=Car('make_of_car2','model_of_car2' , 2002, 'QWERTY123(2)', 100,4,'diesel')
# #print(car1.display_details())
# VehicleInventory1=VehicleInventory()
# VehicleInventory1.add_vehicle(car1)
# VehicleInventory1.add_vehicle(car2)
# VehicleInventory1.display_all()






# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Point(self.x+other.x,self.y+other.y)
#     def __str__(self):
#         return f'({self.x} , {self.y}) is the new point.'
# Point1=Point(1,2)
# Point2=Point(3,4)
# Point3=Point(5,6)
# p4=Point1+Point2
# print(p4+Point3)


# class num:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def func(self):
#         if self.num1>self.num2:
#             for x in range(self.num1,(self.num1*self.num2)+1):
#                 if x%self.num1==0 and x%self.num2==0:
#                     return x
#         else:
#             for y in range(self.num2,(self.num1*self.num2)+1):
#                 if y%self.num1==0 and y%self.num2==0:
#                     return y


# z=num(6,10)
# print(z.func())


# my_string='hi hello!'
# x=my_string.split('e')
# print(x)

# for x in range(10):
#     a=random.randint(1,5)
#     print(a)

# for x in range(1,4):
#     print('*'* x)
#     print()
    
# day=['mon','tue','wed','thu','fri']
# print(day[-3:-1])

#list1=[1,2,3,4,5,4,3,2,1]
# def rev(a):
#     revlist=[]
#     revlist=a[::-1]
#     return revlist
# print(rev(list1))

#fact with while loop 

# def fact(a):
#     x=a
#     val=1
#     while x>1:
#         val*=x
#         x-=1
#     return val

# print(fact(10))

# def listfunc(a):
#     list2=[]
#     for x in a:
#         if x%2==0:
#             list2.append(x)
#     list2.sort()
#     return list2
# print(listfunc(list1))


# class Rect():
#     def __init__(self,h:float,w:float):
#         self.height=h
#         self.width=w
#     def get_area(self):
#         return self.height*self.width
#     def get_peri(self):
#         return 2*(self.height+self.width)
#     def is_square(self):
#         return self.height==self.width
# #r=Rect(50.0,50.0)
# #print(r.get_area(),r.get_peri(),r.is_square(),sep='\n')
        
# class square(Rect):
#     def __init__(self,side):
#         self.height=side
#         self.width=side
# r=square(50)
# print(r.get_area(),r.get_peri(),r.is_square(),sep='\n')