
#this is used to import functions from another python file
from Shashankreddy_SrinivasaReddy_Stats import mean, median, mode1
        
    

#main    
f=open('500DayFruitData.txt','r')
a=f.readline()
lisa=[]
lisb=[]
liss=[]
lisall=[]
for x in range(500):
    b=f.readline()
    g=b.split()
    if g[1]=='apple':
        #count+=1
        lisa.append(int(g[2]))
        lisall.append(int(g[2]))
    if g[1]=='banana':
        lisb.append(int(g[2]))
        lisall.append(int(g[2]))
    if g[1]=='strawberry':
        liss.append(int(g[2]))
        lisall.append(int(g[2]))
    # if g[1]=='strawberry' or g[1]=='banana' or g[1]=='apple':
    #     lisall.append(int(g[2]))


    
    
           
#just for referance
"""print(lisa)
print(lisb)
print(liss)"""
#just for referance




print('The mean number of apples eaten is:',f'{mean(lisa):.2f}')
print('The median number of apples eaten is:',median(lisa))
print('The mode of the apple is',mode1(lisa))
print('The mean number of banana eaten is:',f'{mean(lisb):.2f}')
print('The median number of banana eaten is:',median(lisb))
print('The mode of the banana is',mode1(lisb))
print('The mean number of strawberry eaten is:',f'{mean(liss):.2f}')
print('The median number of strawberry eaten is:',median(liss))
print('The mode of the strawberry is',mode1(liss))
print('The mean number of all eaten is:',f'{mean(lisall):.2f}')
print('The median number of all eaten is:',median(lisall))
print('The mode of all eaten is',mode1(lisall))

meaapple=('The mean number of apples eaten is:'+f'{mean(lisa):.2f}'+'\n')
medapple=('The median number of apples eaten is:'+f'{median(lisa)}'+'\n')
modapple=('The mode of the apple is'+mode1(lisa))
meabanana=('The mean number of banana eaten is:'+f'{mean(lisb):.2f}'+'\n')
medbanana=('The median number of banana eaten is:'+str(median(lisb))+'\n')
modbanana=('The mode of the banana is'+mode1(lisb))
meastrawberry=('The mean number of strawberry eaten is:'+f'{mean(liss):.2f}'+'\n')
medstrawberry=('The median number of strawberry eaten is:'+str(median(liss))+'\n')
modstrawberry=('The mode of the strawberry is'+mode1(liss))
meaall=('The mean number of all eaten is:'+f'{mean(lisall):.2f}'+'\n')
medall=('The median number of all eaten is:'+str(median(lisall))+'\n')
modall=('The mode of all eaten is'+mode1(lisall))

f.close()

r=open('ShashankReddy_SrinivasaReddy_Output.txt' ,'w')
r.write(meaapple)
r.write(medapple)
r.write(modapple)

r.write('\n'*2)
r.write(meabanana)
r.write(medbanana)
r.write(modbanana)
r.write('\n'*2)
r.write(meastrawberry)
r.write(medstrawberry)
r.write(modstrawberry)
r.write('\n'*2)
r.write(meaall)
r.write(medall)
r.write(modall)



r.close()
    


    
