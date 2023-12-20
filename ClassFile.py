
"""#Name
#Shashank Reddy
#Date
#03/24/2023

#This implements the RoboFriend class.
"""
class RoboFriend:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def stateName(self):
        return 'Hello. My name is '+self.name
    def stateAge(self):
        return 'I\'m '+str(self.age)+' years old.'
    


